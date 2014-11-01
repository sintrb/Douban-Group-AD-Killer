# -*- coding: UTF-8 -*
'''
Created on 2014年9月27日

@author: RobinTang
'''
import jieba
from jieba import posseg
def cut(snt):
    words = jieba.cut(snt)
    uwords = set(filter(lambda x: len(x.strip()), words))
    return uwords


if __name__ =='__main__':
    for w in posseg.cut('我爱北京天安门'):
        print w.word, w.flag