from flask import Blueprint
from flask import Flask
from bluprint_moulds import friend_mould, news_mould, admin

app = Flask(__name__)

# 设置域名
# app.config['SERVER_NAME'] = 'example.com:5000'


@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/index')
def index():
    return "通过域名访问"

app.register_blueprint(friend_mould.friend)
app.register_blueprint(news_mould.news)
app.register_blueprint(admin.ad)

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', debug=True)
