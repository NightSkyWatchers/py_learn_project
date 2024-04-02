from flask import Flask, request, render_template, abort, jsonify, redirect, url_for
from werkzeug.routing import BaseConverter  # 导入转换器的基类，用于继承方法

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return 'hello world'


@app.route("/name", methods=['GET'])
def return_json():
    return jsonify({'name': 'zhangsan'})


@app.route("/home_page", methods=['GET'])
def homepage():
    return render_template('homepage.html')


@app.route('/redirect', methods=['GET'])
def redirect2home():
    # redirect重定位（服务器向外部发起一个请求跳转）到一个url界面；
    # url_for给指定的函数构造 URL；
    # 不建议这样做, 将界面限死了
    # return redirect('/home_page')
    # 参数一中的视图名实质指的是endpoint，url_map中存储了url到endpoint的映射，只是默认情况下endpoint与视图函数名相同；
    return redirect(url_for('homepage'))


@app.route('/abort', methods=['GET'])
def abort_func():
    abort(404)
    return None


@app.before_request
def before_request_a():
    print('before_request')

@app.after_request
def after_request_a(response):
    print('after_request')
    # 该装饰器接收response参数，运行完必须归还response，不然程序报错
    return response


# 只有在请求上下文被 pop 出请求栈的时候才会直接跳转到teardown_request；
# 所以在被正常调用之前，即使某次请求有抛出错误，该请求也都会被继续执行, 并在执行完后返回 response；
@app.teardown_request
def teardown_request_a(exc):
    print('I am in teardown_request_a')


# 自定义错误处理方法,将404这个error与Python函数绑定
# 当需要抛出404error时，将会访问下面的代码
@app.errorhandler(404)
def errorhandler_404(err):
    return render_template('404.html')


@app.errorhandler(500)
def errorhandler_500(err):
    return render_template('404.html')


if __name__ == '__main__':
    # 启动一个本地开发服务器，激活该网页
    app.run()
    # app.run(host='0.0.0.0', port=5000, debug=True)
