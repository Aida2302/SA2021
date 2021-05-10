from sqlalchemy.sql import functions
from dataclasses import dataclass

from .database import db


@dataclass
class Student(db.Model):
    id: int
    name: str
    register_time: str

    id = db.Column(db.BigInteger(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    register_time = db.Column(
        db.DateTime(timezone=True), default=functions.now(), nullable=False
    )
    __tablename__ = "students"
