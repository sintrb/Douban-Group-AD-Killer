# -*- coding: UTF-8 -*
'''
Created on 2014年10月20日

@author: RobinTang
'''

from django.db import models
from datamining.classify import BaseDriver

class Probability(models.Model):
    cls = models.CharField(max_length=255)
    prt = models.FloatField(default=0.0)
    atb = models.ForeignKey('Attribute')

class Attribute(models.Model):
    atb = models.CharField(max_length=255)
    count = models.IntegerField(default=0)
    
    def all_probability(self):
        return Probability.objects.filter(atb_id=self.id)
    def get_probability(self, cls):
        rss = Probability.objects.filter(atb_id=self.id, cls=cls)
        return len(rss) and rss[0] or Probability(cls=cls, prt=0.0, atb=self)

class Sample(models.Model):
    cls = models.CharField(max_length=255)
    text = models.TextField()

class Drive(BaseDriver):
    def has_sample(self, text):
#         return len(Sample.objects.filter(text=text))
        return True
    def add_sample(self, text, cls):
        sample = Sample(cls=cls, text=text)
        sample.save()
        return sample
    def all_class(self):
        return Sample.objects.values_list('cls',flat=True).annotate()
    def all_attribute(self):
        return Attribute.objects.values_list('atb',flat=True).annotate()
    def has_attribute(self, atb):
        return len(Attribute.objects.filter(atb=atb))
    def get_attribute(self, atb):
        at = Attribute.objects.filter(atb=atb).first()
        if not at:
            at = Attribute(atb=atb,count=0)
            at.save()
        return at



    
    
    