USERNAME='root'
PASSWORD='12345'
HOST='127.0.0.1'
PORT='3306'
DATABASE='flaskdb'
# 创建URI（统一资源标志符）
'''
SQLALCHEMY_DATABASE_URI的固定格式为：
'{数据库管理系统名}://{登录名}:{密码}@{IP地址}:{端口号}/{数据库名}?charset={编码格式}'
'''
DB_URI = 'mysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOST,PORT,DATABASE)

# 设置动态追踪修改,如未设置只会提示警告
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 设置查询时会显示原始SQL语句
SQLALCHEMY_ECHO = True
