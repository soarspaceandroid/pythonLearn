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


#math 模块
import math
log(dir(math))

#系统模块
import sys
log(dir(sys))
import os
log(dir(os))

#内置模块(不用import就可以直接使用)常用内置函数：
#help(obj) 在线帮助, obj可是任何类型    
#callable(obj) 查看一个obj是不是可以像函数一样调用    
#repr(obj) 得到obj的表示字符串，可以利用这个字符串eval重建该对象的一个拷贝    
#eval_r(str) 表示合法的python表达式，返回这个表达式    
#dir(obj) 查看obj的name space中可见的name    
#hasattr(obj,name) 查看一个obj的name space中是否有name    
#getattr(obj,name) 得到一个obj的name space中的一个name    
#setattr(obj,name,value) 为一个obj的name   
#space中的一个name指向vale这个object    
#delattr(obj,name) 从obj的name space中删除一个name    
#vars(obj) 返回一个object的name space。用dictionary表示    
#locals() 返回一个局部name space,用dictionary表示    
#globals() 返回一个全局name space,用dictionary表示    
#type(obj) 查看一个obj的类型    
#isinstance(obj,cls) 查看obj是不是cls的instance    
#issubclass(subcls,supcls) 查看subcls是不是supcls的子类  

##################    类型转换  ##################

#chr(i) 把一个ASCII数值,变成字符    
#ord(i) 把一个字符或者unicode字符,变成ASCII数值    
#oct(x) 把整数x变成八进制表示的字符串    
#hex(x) 把整数x变成十六进制表示的字符串    
#str(obj) 得到obj的字符串描述    
#list(seq) 把一个sequence转换成一个list    
#tuple(seq) 把一个sequence转换成一个tuple    
#dict(),dict(list) 转换成一个dictionary    
#int(x) 转换成一个integer    
#long(x) 转换成一个long interger    
#float(x) 转换成一个浮点数    
#complex(x) 转换成复数    
#max(...) 求最大值    
#min(...) 求最小值  



# import model from other python file
from soarmodel import model1
log(model1(5))



# global globvar    # 使用 global 声明全局变量
global age
age = 16

#文件操作
fo = open("soarmodel.py","wb") #wb 是 访问这个文件的mode , 是只读还是读写操作
log(fo.name)
#下面写入一段代码
fo.write("#!/usr/bin/python
# -*- coding: UTF-8 -*-

def model1(para):
    return 10+para

def getname():
    return soar

def renamefile(file):
    fe = open(file,"wb")
    fe.rename(file,"gaofeitest.py")

")
fo.close()


content = open("soarmodel.py","r+") #wb 是 访问这个文件的mode , 是只读还是读写操作
log(content.name)
log(content.read())
content.close()






