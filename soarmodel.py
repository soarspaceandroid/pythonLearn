#!/usr/bin/python
# -*- coding: UTF-8 -*-

class soarmodel:
    def __init__(self,para):
        return self.model1(para)

    def model1(para):
        return 10+para

    def getname(name):
        return "soar--"+name

    def renamefile(file):
        fe = open(file,"wb")
        fe.rename(file,"gaofeitest.py")
