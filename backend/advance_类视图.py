from abc import ABC

from flask import Flask, request, render_template, views, typing as ft

app = Flask(__name__)


class Alert(views.View):
    def __init__(self):
        super(Alert, self).__init__()
        self.instance_attribute = {
         'alert': 'This is an alert message'
        }


class Index(Alert):

    def dispatch_request(self) -> ft.ResponseReturnValue:
        return render_template('class_mould/index.html', **self.instance_attribute)

class Login(Alert):

    def dispatch_request(self) -> ft.ResponseReturnValue:
        return render_template('class_mould/login.html', **self.instance_attribute)


class Register(Alert):

    def dispatch_request(self) -> ft.ResponseReturnValue:
        return render_template('class_mould/register.html', **self.instance_attribute)


app.add_url_rule(rule='/', endpoint='index', view_func=Index.as_view('index'))
app.add_url_rule(rule='/login', endpoint='login', view_func=Login.as_view('login'))
app.add_url_rule(rule='/register', endpoint='register', view_func=Register.as_view('register'))


if __name__ == '__main__':
    # 启动一个本地开发服务器，激活该网页
    # print(app.view_functions)

    app.run(host='0.0.0.0', port=5002, debug=True)
