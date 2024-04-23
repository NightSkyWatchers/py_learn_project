from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from backend.sqlalchemy.循环引用config import Config
from backend.sqlalchemy.models import User
# 解除循环引用
from backend.sqlalchemy.循环引用config import db

app = Flask(__name__)

# 循环引用
# app.config.from_object(Config)
#
# db = SQLAlchemy(app)


# 解除循环引用
app.config.from_object(Config)
db.app = app
db.init_app(app)




@app.route('/')
def hello_world():
    db.drop_all()
    db.create_all()
    return 'Hello world!'

if __name__ == '__main__':
    app.run(debug=True)