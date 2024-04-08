from flask import Flask, request, render_template, views, typing as ft

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


class LoginView(views.MethodView):
    # 定义get方法
    def get(self):
        return render_template('method_view_mould/login.html')

    # 定义post方法
    def post(self):
        user_name = request.form.get('username')
        password = request.form.get('password')

        if user_name == 'admin' and password == '123456':
            return '登录成功'
        else:
            return '登录失败'


app.add_url_rule('/login', view_func=LoginView.as_view('login'))

if __name__ == '__main__':
    # 启动一个本地开发服务器，激活该网页
    # print(app.view_functions)

    app.run(host='0.0.0.0', port=5004, debug=True)
