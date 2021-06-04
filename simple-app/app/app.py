from flask import Flask, request, redirect, jsonify
from models import db, Student
import os

app = Flask(__name__)
# app.config.from_json("config.json")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URI', '')
app.config["VERIFY_SSL"] = False

db.init_app(app)


def to_array(all_vendors):
    v = [ven.as_dict() for ven in all_vendors]
    return v


@app.route('/health-check')
def hello_world():
    print(app.config["SQLALCHEMY_DATABASE_URI"] + ' Aida')
    print("health check")
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
    return jsonify(to_array(students))


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
    print(student)
    if student:
        db.session.delete(student)
        db.session.commit()
    return redirect("/")


if __name__ == '__main__':
    app.run()
