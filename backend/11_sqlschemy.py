from datetime import datetime

from django.template.defaultfilters import first
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin123@localhost/flask_db1?charset=utf8mb3"

db = SQLAlchemy(app)



# 创建表模型类对象
class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 定义id字段
    title = db.Column(db.String(50), nullable=False)  # 定义title字段
    publishing_office = db.Column(db.String(100), nullable=False)  # 定义出版社字段
    price = db.Column(db.String(30), nullable=False)  # 定义price号字段
    isbn = db.Column(db.String(50), nullable=False)  # 定义isbn号字段
    storage_time = db.Column(db.DateTime, default=datetime.now)  # 入库时间字段



@app.route('/')
def index():
    # db.drop_all()
    # db.create_all()
    return 'create tables'

@app.route('/add')
def add_record():
    book1 = Book(title='Python基础教程(第3版)', publishing_office='人民邮电出版社', price='68.30 ', isbn='9787115474889')
    book2 = Book(title='Python游戏编程快速上手第4版', publishing_office='人民邮电出版社', price='54.50', isbn='9787115466419')
    book3 = Book(title='JSP+Servlet+Tomcat应用开发从零开始学', publishing_office='清华大学出版社', price='68.30',
                 isbn='9787302384496')

    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    # 需要提交事务给数据库
    db.session.commit()
    return 'add success!'

@app.route('/query')
def query_record():
    # result = db.session.query(Book.id=1).all()
    # result = Book.query.filter(Book.id == 1).first()
    result = Book.query.filter(Book.isbn == '9787302384496').first()
    print(result.title)

    result_list = Book.query.filter(Book.publishing_office == '人民邮电出版社').all()
    for books in result_list:
        print(books.title)
    return 'query success'


@app.route('/edit')
def edit_record():
    # result = db.session.query(Book.id=1).all()
    # result = Book.query.filter(Book.id == 1).first()
    book1 = Book.query.filter(Book.id == 1).first()
    book1.price = 0.1
    db.session.commit()
    return 'edit success'


@app.route('/delete')
def delete_record():

    book2 = Book.query.filter(Book.id == 2).first()
    db.session.delete(book2)
    db.session.commit()
    return 'delete success'


if __name__ == '__main__':
    app.run(debug=True)


