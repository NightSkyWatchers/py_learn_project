from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.config import Config
app = Flask(__name__)


# app.config.from_object(Config)
# db = SQLAlchemy(app)
# 打印结果：mysql+pymysql://root:***@127.0.0.1:3306/flaskdb?charset=utf8mb3

db = SQLAlchemy()

# 在使用了db.app = app后，
# 我们甚至可以把配置文件的导入操作放在db = SQLAlchemy()后面，
# 因为这一步就是将db对象的app属性指向了我们的flask对象——app，
# 后续对flask对象的修改也就是对db.app属性的修改（对象传参，传的是指针），
# 但是要注意导入配置的操作要在db.init_app(db)前执行。

app.config.from_object(Config)
db.app = app
db.init_app(app)

with app.app_context():
    print(db.engine.url)

if __name__ == '__main__':
    app.run(debug=True)