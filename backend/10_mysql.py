from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy.config import Config

app = Flask(__name__)

# 初始化数据库配置
# 1. 直接用键值对插入配置：（使用 localhost 替代 127.0.1:3306）
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin123@localhost/flaskdb?charset=utf8mb3"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_ECHO'] = True


# 2.定义配置类后导入：（使用localhost替代127.0.1: 3306）
app.config.from_object(Config)
print(app.config)

# 初始化一个SQLAlchemy对象
db = SQLAlchemy(app)
# db = SQLAlchemy()
# db.app = app
# db.init_app(app)

print(db)


class User(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    # db.String==> db.String(50) VARCHAR requires a length on dialect mysql
    username: Mapped[str] = mapped_column(db.String(50), unique=True, nullable=False)


# 使用SQLALchemy创建表book
class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(30), nullable=False)


with app.app_context():
    # 可以在前面添加一行drop_all()
    # 代码来删除已经创建的表
    db.drop_all()
    # 测试数据库连接是否成功（create_all将我们定义的所有表类映射为数据库下的表）

    db.create_all()
    book = Book(id=1, name='Python编程1', author='张三')
    user = User(id=3, username='l')

    db.session.add(user)
    db.session.add(book)

    db.session.commit()
