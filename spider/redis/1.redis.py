from redis import Redis
import  json

con = Redis(host='127.0.0.1',port=6379,
            # password='123123',
            db=0,decode_responses=True)

# r = con.set(name='wuyi', value='laodongjie1')
# print(con.get(name='wuyi'))
# print(con.keys())


# con.hset('py_wusir','name','wupeiqi',)
# con.hset('py_wusir','age',18)
#
# r0 = con.hget('py_wusir','name')
# print(r0)# b'wupeiqi'

# r1 = con.hgetall('py_wusir')
# print(r1)#{b'name': b'wupeiqi', b'age': b'18'}

# con.hset('py_wusir2',mapping={'name':'wupeiqi','age':18,'height':170})
# print(con.hgetall('py_wusir2'))# {'name': 'wupeiqi', 'age': '18', 'height': '170'}


# list1 = ['laodongjie', 'qingmingjie', 'guoqingjie', 'chunjie']
#
# con.lpush('py_jieri', *list1)
#
# list2 = ['shengdanjie', 'qingrenjie', 'yuandanjie']
#
# con.rpush('py_jieri',*list2)

# print(con.lrange(name='py_jieri', start=0, end=-1))

# con.zadd(name='py_yan',mapping={'yunyan':10,'zhonghua':100,'yuxi':20})
# r = con.zrange('py_yan',start=0,end=3)
# print(r)


# 存储列表、字典或者列表套字典
# 1. set存
lst = ['zhangsan','lisi','wuer','mazi']
con.set('py_mingzi',json.dumps(lst))

print(con.get('py_mingzi'))

lst2 = ['张三','lisi','wuer','mazi']
con.set('py_mingzi2',json.dumps(lst2))

print(json.loads(con.get('py_mingzi2')))


con.close()