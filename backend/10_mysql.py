from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import sqlconfig.config1

app = Flask(__name__)

# 初始化数据库配置

#1. 直接用键值对插入配置：（使用 localhost 替代 127.0.1:3306）
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.1:3306/flaskdb?charset=utf16'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True


# 2.定义配置类后导入：（使用localhost替代127.0.1: 3306）

# class Config:
#     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123@localhost/flaskdb?charset=utf16'
#     SQLALCHEMY_TRACK_MODIFICATIONS = True
#     SQLALCHEMY_ECHO = True
#
# app.config.from_object(sqlconfig.config1)



# 初始化一个SQLAlchemy对象
db = SQLAlchemy(app)
# db = SQLAlchemy()
# # 源代码中还包含self.app=app这条语句，所以添加此语句:
# db.app = app

print(db)

# # 初始化app对象中与数据库相关的配置的设置，防止数据库信息泄露
db.init_app(app)
db.create_all()


# # 使用SQLALchemy创建表book
# class Book(db.Model):
#     __tablename__ = 'book'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(50), nullable=False)
#     author = db.Column(db.String(30), nullable=False)
#     publication_date = db.Column(db.Date, nullable=False)
#     isbn = db.Column(db.String(13), nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     storage_time = db.Column(db.DateTime, nullable=False, default=db.func.now())


@app.route('/')
def index():
    return 'index'

# if __name__ == '__main__':
    # app.run(debug=True)

    # 可以在前面添加一行drop_all()代码来删除已经创建的表
    # db.drop_all()
    # # 测试数据库连接是否成功（create_all将我们定义的所有表类映射为数据库下的表）
    # db.create_all()
    # book = Book(id=1, name='Python编程', author='张三', publication_date='2021-01-01', isbn='978-7-121-3456-789', price=99.99)
    # db.session.add(book)
    # db.session.commit()