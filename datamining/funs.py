# -*- coding: UTF-8 -*
'''
Created on 2014年9月27日

@author: RobinTang
'''
from third import jieba
def cut(snt):
    words = jieba.cut(snt)
    uwords = set(filter(lambda x: len(x.strip()), words))
    return uwords
    