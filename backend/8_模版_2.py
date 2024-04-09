from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def 多参数传递():

    name= 'John Doe'
    age= 30
    # 如果有多个变量需要传递，我们可以不需要一个一个进行传参，直接使用 ** locals()
    # 替代我们在当前视图函数中定义的所有变量：
    return render_template('模版/index2.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)