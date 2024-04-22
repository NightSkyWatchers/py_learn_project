from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)

# 或替换为 mysql+pymysql （使用 localhost 替代 127.0.1:3306）
DATABASE_URL = "mysql+pymysql://root:admin123@localhost/db_test?charset=utf8mb4"
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app=app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    pw_hash = db.Column(db.String(80))


with app.app_context():
    print('=======>')
    db.drop_all()
    db.create_all()

    user = User(id=1, username='admin2', pw_hash='pbkdf2')
    db.session.add(user)
    db.session.commit()





