from flask import Flask, request, render_template, abort, jsonify, redirect, url_for
from werkzeug.routing import BaseConverter  # 导入转换器的基类，用于继承方法

app = Flask(__name__)


@app.route('/helloworld', endpoint='hi')
# 底层其实是使用add_url_rule实现的
def hello_world():
    return 'Hello World!'


def advance_home():
    return '高级用法_add_url_rule的首页'


app.add_url_rule(rule='/', endpoint='index', view_func=advance_home)

# 请求上下文只有在发送request请求时才会被激活，激活后request对象被设置为全局可访问
# 其内部封装了客户端发出的请求数据报文
# 此处是主动生成一个临时的测试请求上下文
# with app.test_request_context():
#     print(url_for('index'))  # 输出结果为/

if __name__ == '__main__':
    # 启动一个本地开发服务器，激活该网页
    app.run(host='0.0.0.0', port=5001, debug=True)
