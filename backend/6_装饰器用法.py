import flask
from functools import wraps


app = flask.Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


#  预登录操作
def user_login(func):
    # 保留原函数的属性与名称
    @wraps(func)
    # 无参数
    # def inner():
    #     print("user_login操作")
    #     func()
    # 传参
    #     * ：代表元组，长度不限；
    #     ** ：代表键值对，个数不限；
    #     *args：指用元组传参，元组内包含不定个数的位置参数；
    #     ** kwargs：指用字典传参，字典内包含不定个数的关键字参数（键值对）；
    def inner(*args, **kwargs):
        print("user_login操作")
        func(*args, **kwargs)

    return inner


def friend_list():
    print(f'函数名：{friend_list.__name__}')
    print("friend_list")


# 装饰器用法
@user_login
def friend_list_2():
    print(f'函数名：{friend_list_2.__name__}')
    print("friend_list_2")

@user_login
def friend_list_3(name):
    print(f'函数名：{friend_list_3.__name__}')
    print(f"{name}的friend_list_3")

if __name__ == '__main__':
    # 调用方法1
    # 此处的t为函数 ,t()调用函数
    t = user_login(friend_list)
    t()

    # 调用方法2
    friend_list_2()

    # 调用方法3
    friend_list_3("张三")
    app.run(debug=True)
