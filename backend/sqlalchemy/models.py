# from backend.sql循环引用 import db
from backend.sqlalchemy.循环引用config import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    telephone = db.Column(db.String(11), nullable=False)
