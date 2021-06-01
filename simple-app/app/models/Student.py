from sqlalchemy.sql import functions
from collections import OrderedDict
from .database import db


class Student(db.Model):
    id = db.Column(db.BigInteger(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    register_time = db.Column(
        db.DateTime(timezone=True), default=functions.now(), nullable=False
    )
    __tablename__ = "students"

    def as_dict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result
