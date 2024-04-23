from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin123@localhost/flask_db2?charset=utf8mb3"

db = SQLAlchemy(app)


# 1. 创建一对一关系，外键和relationship都可以由相关联的两个表模型中，任意一个表模型添加；
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)


# 学生证
class IDCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_no = db.Column(db.String(20), unique=True)
    stu_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    stu = db.relationship('Student', backref=db.backref('id_card'), uselist=False)


# 2.创建一对多关系，外键必须由相关联的两个表模型中，“多”对应的表模型添加；
# relationship则需要由“少”对应的表模型添加
class Writer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    # 通过relationship方法与Book表建立起关系
    # Writer表的实例对象，可以通过books属性，查找到Book表中外键绑定了自身id的多条书本信息
    # Book表的实例对象，可以通过writers属性，查找到外键writer_id对应的Writer表中的单条作者信息
    books = db.relationship('Book', backref=db.backref('writer'))


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    publish_office = db.Column(db.String(50), default='人民大学')
    # 在Book表中添加外键，绑定Writer表的主键id（表名不区分大小写）
    writer_id = db.Column(db.Integer, db.ForeignKey('writer.id'))


# 3. 创建多对多关系，则需单独创建一个存储关联关系的表（不需要构建表模型类，
# 直接用db.Table()方法实例化一个表对象），并在这个表中添加外键来绑定它所连接的表；
# relationship则可以由相关联的两个表模型中的任意一个添加；

# 实例化一个关联关系表对象
# 等号前的book_tag是Table对象名，等号后的参数一 book_tag是表名
tag = db.Table('factory_wanju_tag', db.Column('wanju_id', db.Integer, db.ForeignKey('wanju.id')),
               db.Column('factory_id', db.Integer, db.ForeignKey('factory.id')))


# 工厂表
class Factory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(10))
    wanju = db.relationship('Wanju', secondary=tag, backref=db.backref('factory'))


# 玩具表
class Wanju(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.Integer, default=0)
    name = db.Column(db.String(10))


@app.route('/')
def index():
    db.drop_all()
    db.create_all()

    writer = Writer(name='张三')
    writer2 = Writer(name='李四')



    db.session.add(writer)
    db.session.add(writer2)

    book1 = Book(title='python_book', writer_id=1)
    book2 = Book(title='java_book', writer_id=1)
    book3 = Book(title='ios_book', writer_id=2)
    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)

    db.session.commit()
    return 'create tables'

@app.route('/query')
def query_writer():
    writer = Writer.query.filter(Writer.id == 1).first()
    print(writer.name)
    for book in writer.books:
        print(book.title)

    return 'query'


if __name__ == '__main__':
    app.run(debug=True)
