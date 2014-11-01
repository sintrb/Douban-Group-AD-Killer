# -*- coding: UTF-8 -*
'''
Created on 2014年10月28日

@author: RobinTang
'''

from django.db import models

class GroupTopic(models.Model):
    tid = models.CharField(max_length=16, db_index=True)
    url = models.CharField(max_length=255)
    uid = models.CharField(max_length=16, db_index=True)
    gid = models.CharField(max_length=16, db_index=True)
    title = models.CharField(max_length=255, db_index=True)
    text = models.TextField()
    created = models.CharField(max_length=32)
    type = models.CharField(max_length=16)
    other = models.CharField(max_length=255)





