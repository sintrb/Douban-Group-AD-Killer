# -*- coding: UTF-8 -*
'''
Created on 2014年10月28日

@author: RobinTang
'''

from django.db import models

class GroupTopic(models.Model):
    tid = models.CharField(max_length=16)
    url = models.CharField(max_length=16)
    title = models.CharField(max_length=255)
    text = models.TextField()
    type = models.CharField(max_length=16)
    other = models.CharField(max_length=255)