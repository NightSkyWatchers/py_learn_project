from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base # 1.4之前是 from sqlalchemy.ext.declarative import declarative_base
from flask import Flask
import pymssql

app = Flask(__name__)

DATABASE_URL = 'mssql+pymysql://root:123456@127.0.1:3306/flaskdb'  # 或替换为 mysql+mysqlconnector

engine = create_engine(DATABASE_URL, echo=False)
# Session = sessionmaker(bind=engine)
# session= Session()

connection = engine.connect()

Base = declarative_base()


# 定义表模型
class YourTable(Base):
    __tablename__ = 'your_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer)


if __name__ == '__main__':
    # 创建数据库（如果不存在） & 选择数据库

    # engine.execute("CREATE DATABASE IF NOT EXISTS flaskdb")
    # engine.execute("USE flaskdb")

    connection.execution_options("CREATE DATABASE IF NOT EXISTS flaskdb")
    # engine.execution_options("USE flaskdb")

    # 创建表
    Base.metadata.create_all(engine)


