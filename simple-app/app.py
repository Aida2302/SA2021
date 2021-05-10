from flask import Flask, request, redirect, jsonify

from models import db, Student


app = Flask(__name__)
app.config.from_json("config.json")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route('/health-check')
def hello_world():
    return 'Hello World!'


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        try:
            data = request.get_json()
            name = data['name']
            student = Student(name=name)
            db.session.add(student)
            db.session.commit()
        except Exception as e:
            print("Failed to add student")
            print(e)

    students = Student.query.all()
    return jsonify(students)


@app.route("/update", methods=["PUT"])
def update():
    try:
        data = request.get_json()
        id_ = data['id']
        name = data['name']
        student = Student.query.filter_by(id=id_).first()
        student.name = name
        db.session.commit()
    except Exception as e:
        print("Couldn't update student's name")
        print(e)
    return redirect("/")


@app.route("/delete", methods=["DELETE"])
def delete():
    data = request.get_json()
    id_ = data['id']
    student = Student.query.filter_by(id=id_).first()
    db.session.delete(student)
    db.session.commit()
    return redirect("/")


if __name__ == '__main__':
    app.run()
