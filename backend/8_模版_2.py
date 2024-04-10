from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index2():

    name= 'John Doe'
    age= 30
    # 如果有多个变量需要传递，我们可以不需要一个一个进行传参，直接使用 ** locals()
    # 替代我们在当前视图函数中定义的所有变量：
    return render_template('模版/index2.html', **locals())

@app.route('/if')
def index3():
    # jinja2模板引擎中也可使用if和for控制语句，但是语句需要放置在
    # { % %}中；
    #
    # if条件判断语句必须包含结束标签
    # { % endif %}，其他部分与python中类似，可以与比较运算符 > >= < <= == != 结合使用，或与逻辑运算符and, or, not, ()
    # 结合使用；
    name= 'John Doe'
    return render_template('/模版/index3.html', **locals())


@app.route('/for')
def index4():
    # for循环控制语句在模板内的用法也和python中类似，遍历的对象可以是字典、元组、列表等，但需要注意的是在模板中无法使用continue和break来对循环进行控制；
    # for循环的内置常量：
    # loop.index: 获取当前的索引值 从1开始
    # loop.index0:获取当前的索引值 从0开始
    # loop.first: 判断当前是否是第一次迭代, 是返回True否则返回False
    # loop.last: 判断当前是否是最后一次迭代, 是返回True否则返回False
    # loop.length: 序列的长度

    users = ['name', 'age', 'height', 'weight']
    return render_template('/模版/index4.html', **locals())




@app.route('/filter')
def index5():
    # 常用过滤器有哪些？
    # 可以在前端模板内{{ 内容 | 过滤器 }}的" | "后使用；
    # 可以使用add_template_filter(函数方法名,'过滤器名')来自定义过滤器；

    user = ['name', 'age', 'height', 'weight']
    return render_template('/模版/index5.html', **locals())

# 自定义过滤器
def reverse_list(li:list ):
    li.reverse()
    return li

# 注册模板过滤器（filter）
# 参数1为该过滤器调用的函数，参数2为在前端中调用该过滤器使用的名称
app.add_template_filter(reverse_list,'reverse')



@app.route('/macro')
def index6():
    # 宏的定义是为了将前端模板中需要反复创建的模块变成一个方便调用的“函数”，这一操作类似于python中创建函数，也可以传参，但不能有返回值；
    # 宏的定义以macro标志开始，以endmacro结束，同样需要在{% %}中进行。

    return render_template('/模版/index6.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)