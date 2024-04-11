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


@app.route('/macro1')
def index7():
    # 宏的导入可以使用语句import 模板文件名 as 别名或from 模板文件名 import 宏名称，就像python中库和包的导入一样；
    # 我们将宏单独定义在一个html模板文件中后，就可以通过导入这个模板文件来调用里面的所有宏，导入过程同样在{% %}中进行，调用过程在{{ }}在进行。

    return render_template('/模版/index7.html', **locals())



@app.route('/include')
def index8():
    # include用于在一个模板的指定位置导入另一个模板的内容，
    # 区别于宏的调用，include更像从另一个模板“复制+粘贴”；
    # include同样在{% %}中使用，采用语句{% include 模块名 %}
    #include是直接将目标模板中的所有内容直接“copy”在当前位置，
    # 所以被导入的模板如果有head和body部分也将被导入过来；
    #include和import都是在templates这个目录下搜索的，
    # 所以使用路径时不需要添加相对路径：上级目录 “ …/ ” 和当前目录 “ ./ ” ；
    name = '张三'
    return render_template('/模版/index8.html', **locals())



@app.route('/setwith')
def index9():
    # set——自定义全局变量：由set定义的变量可以在模板内任意一个地方调用，甚至在子模板中也可以使用；
    # with——自定义局部变量：with定义的变量只能在{% with %}到{% endwith %}这个代码块间使用；
    return render_template('/模版/index9.html')


@app.route('/static')
def index10():
    # 静态文件一般是我们在开发过程中用到的图片文件、css文件和js文件，
    # 在Flask工程中通常包含一个static文件目录，
    # 当需要调用静态文件是将会默认在该目录下进行查询，固不需要使用相对路径；
    # 通常我们会在static文件目录下定义名为css、image和js的文件夹分别存储这些静态文件；
    # 加载静态文件通常配合url_for函数使用(需要在双括号内调用)，
    # 将模板标签的src、herf属性通过url_for(静态文件名称)设置为反转url要比使用相对路径更好。

    return render_template('/模版/index10.html')


@app.route('/extend')
def index11():
    #而在extends中，我们当前的模板则是待装载的代码块，
    # 需要我们继承一个框架来搭载这些代码块，
    # 这时候就需要extend来导入框架（基类）模块了；
    return render_template('/模版/extend/father.html')


@app.route('/extend1')
def index12():
    #   在继承操作中，如果子模板实现了父模板的某个block，
    #   那么子模板中该block的代码就会覆写父模板中的代码，
    #   如果我们在子模板中仍然想保留父模板的代码，
    #   可以使用super()方法实现。
    return render_template('/模版/extend/son1.html')


@app.route('/extend2')
def index13():
    #而在extends中，我们当前的模板则是待装载的代码块，
    # 需要我们继承一个框架来搭载这些代码块，
    # 这时候就需要extend来导入框架（基类）模块了；
    return render_template('/模版/extend/son2.html')



if __name__ == '__main__':
    app.run(debug=True)