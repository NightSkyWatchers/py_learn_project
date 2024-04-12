from flask import Flask, render_template, request, flash, redirect, url_for
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

from form import config   # 导入配置文件
from flask_wtf import CSRFProtect,FlaskForm # 导入CSRFProtect模块


app = Flask(__name__)
# 方法1. 定义配置文件，导入配置模块中的配置
# 再将配置文件中的配置语句通过app.config.from_object(<配置对象>)
# 或app.config.from_pyfile(<'配置文件名'>)导入到flask对象app中，
# 这个配置对象可以是配置模块也可以是配置类
# app.config.from_object(config)

# 方法2.直接通过键值对的方式新增配置
# 用于生成动态令牌的秘钥
app.config['SECRET_KEY'] = 'ADJLAJDLA'
# 用于开启CSRF保护，但默认状态下都是开启的
app.config['CSRF_ENABLED'] = True


# 为当前应用程序启用WTF_CSRF保护，并返回一个CSRFProtect对象
csrf = CSRFProtect(app)
#除了使用上述方法来配置CSRF保护，
# 我们还需要用到flask_wtf与wtfroms来定义一个支持CSRF保护的后端表单，
# 我们一般将其定义在一个类当中；该类需要继承基类：flask_wtf.FlaskForm或flask_wtf.Form，
# 二者完全相同，但Form即将被FlaskForm替换，推荐使用前者！

# 定义表单模型类，继承FlaskForm
class Register(FlaskForm):
    # 定义表单中的元素，类似于html的form中定义input标签下的内容
    # label 用于点击后跳转到某一个指定的field框
    # validators 用于接收一个验证操作列表
    # render_kw 用于给表单字段添加属性，各属性以键值对的形式设置
    username = StringField(label='用户名:',
                            validators=[DataRequired(message=u'用户名不能为空'), Length(6, 16, message='长度位于6~16之间')],
                            render_kw={'placeholder': '输入用户名'})
    # message中存放判断为错误时要返回的信息，EqualTo中第一个参数是要比较的field组件
    password = PasswordField(label='密码:',
                             validators=[DataRequired(message=u'密码不能为空'), EqualTo('password2', message=u'两次输入需相同'),
                                         Length(6, 16, message='长度位于6~16之间')], render_kw={'placeholder': '输入密码'})
    password2 = PasswordField(label='再次输入密码:',
                              validators=[DataRequired(message=u'密码不能为空'), Length(6, 16, message='长度位于6~16之间')],
                              render_kw={'placeholder': '再次输入密码'})
    submit = SubmitField(label='提交')


@app.route('/index2', methods=['GET','POST'])
def  index2():
    # 实例化表单对象
    form = Register()
    if request.method == 'GET':
        # 表单对象发送至前端
        return render_template('/form/index2.html', form=form)
    elif request.method == 'POST':
        # form.validate_on_submit() 等价于：request.method=='post' and form.validate()
        # form.validate() 用于验证表单的每个字段（控件），都满足时返回值为True
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            password2 = form.password2.data
            return 'login success'
        else:
            # flask的form使用一个字典来储存各控件的errors列表
            # print(type(form.errors))
            # 输出密码字段导致validate_on_submit为false的错误原因（两种方式）
            print(form.errors['password'])
            print(form.password.errors)
            return render_template('/form/index2.html', form=form)



# --------------视图函数------------------
@app.route('/index3', methods=['GET', 'POST'])
def index3():
    if request.method == 'GET':
        flash('用户名或密码不正确,请检查!')
        return render_template("/form/index3.html")



@app.route('/', methods=['GET', 'POST'], endpoint='index')
def index():

    # 传统的前端通用表单，需要前后端共同完成操作
    if request.method == 'POST':
        # 获取表单中name为username的文本域提交的数据
        name = request.form.get('username')
        # 获取表单中name为password的文本域提交的数据
        password = request.form.get('password')
        return name + " " + password

    # 上述的方法既没有为表单提供保护措施，也不利于前后端分离的改进需求
    # wtforms依照功能类别来说wtforms分别由以下几个类别：
    # Forms: 主要用于表单验证、字段定义、HTML生成，并把各种验证流程聚集在一起进行验证。
    # Fields: 包含各种类型的字段，主要负责渲染(生成HTML文本域)和数据转换。
    # Validator：主要用于验证用户输入的数据的合法性。比如Length验证器可以用于验证输入数据的长度。
    # Widgets：html插件，允许使用者在字段中通过该字典自定义html小部件。
    # Meta：用于使用者自定义wtforms功能（配置），例如csrf功能开启。
    # Extensions：丰富的扩展库，可以与其他框架结合使用，例如django

    if request.method == 'GET':
        return render_template('/form/index.html')



def config():
    pass


if __name__ == '__main__':
    app.run(debug=True)