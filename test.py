#!/usr/bin/python
# -*- coding: UTF-8 -*-

#学习基本知识地址  http://www.runoob.com/python/python-dictionary.html

#简单的参数定义
print "this is test"
name = "gaofei"
print name
print name[2:5]
list = ["soar" , "grace"]
print list

tem = "soar"
if tem == "soar":
    print "true"
else :
    print tem
    

#while 循环
a = 9
while a < 20:
    print "----" , a
    if a%2==0:
        break
    a = a+1


#for循环
#pass 不做任何事情，一般用做占位语句
for  letter in "python":
    if letter == "y":
        continue
    if letter == "h":
        pass
    print letter

#Python 列表(List)
lists = ["this" , "is" , "test"]

#元组
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
print tup1
print tup1[3]
print tup1[1:4]
tup3 = tup1 + tup2;
print tup3
del tup2 #删除元组

#Python 字典(Dictionary)  相当于 map
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict["Alice"] = "54644845458454545448542215445"
print dict["Cecil"]
print dict["Alice"]
print "---------",dict.itervalues


# time 模块
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身
import time #引入time模块
print time.time()
localtime = time.localtime(time.time())
print localtime
print time.strftime("%Y年%m月%d日 %H时%M分%S秒" , time.localtime())

# 函数语法
def getString(str):
    return "----------"+str

def log(params):
    print "log-----> " , params


#  函数调用
print getString("gaofei")

#测试log 调用
log("test  log")




