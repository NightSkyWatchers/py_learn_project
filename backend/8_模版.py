from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'name': 'John Doe',
        'age': 30,
        'nicknames': ['d','do', 'doe']
    }

    # 前端html模板内需要在双括号{{}} 中使用该变量：
    return render_template('模版/index.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)