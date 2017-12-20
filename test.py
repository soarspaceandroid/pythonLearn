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

