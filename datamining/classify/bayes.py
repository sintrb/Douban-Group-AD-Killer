#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-10-15
# @Author  : Robin (sintrb@gmail.com)
# @Link    : https://github.com/sintrb/Douban-Group-AD-Killer
# @Version : 1.0

from base import BaseClassifier, test_classifer

class BaseProbability():
	def __init__(self, cls, prt):
		self.cls = cls
		self.prt = prt

class BaseAttribute(object):
	def __init__(self, atb):
		self.atb = atb
		self.count = 0
		self.map = {}
	def all_probability(self):
		return self.map.values()
	def get_probability(self, cls):
		if cls not in self.map:
			self.map[cls] = BaseProbability(cls, 0.0)
		return self.map[cls] 

class BaseDriver(object):
	def __init__(self):
		self.classes = {}
		self.attributes = {}
	def has_sample(self, sample):
		return sample in self.classes
	def add_sample(self, sample, cls):
		if cls not in self.classes:
			self.classes[cls] = set()
		self.classes[cls].add(sample)
	def all_class(self):
		return self.classes
	def all_attribute(self):
		return self.attributes.values()
	def has_attribute(self, atb):
		return atb in self.attributes
	def get_attribute(self, atb):
		if atb not in self.attributes:
			self.attributes[atb] = BaseAttribute(atb)
		return self.attributes[atb]
	def show_info(self):
		for atb in self.all_attribute():
			for prt in atb.all_probability():
				print '%s -- > %s %s'%(atb.atb, prt.cls, prt.prt)

class NaiveBayesClassifier(BaseClassifier):
	"""朴素贝叶斯分类"""
	def __init__(self, db):
		super(NaiveBayesClassifier, self).__init__()
		self.db = db
		
	def training(self, sample, cls, force=False):
		if not self.db.has_sample(sample) or force:
			self.db.add_sample(sample, cls)
		for a in sample:
			att = self.db.get_attribute(a)
			prt = att.get_probability(cls)
			prt.prt = prt.prt + 1.0/len(sample)
			att.count = att.count + 1
	def classify(self, sample):
		clss = {}
		for c in self.db.all_class():
			clss[c]  = 0.0
		for a in sample:
			if self.db.has_attribute(a):
				atb = self.db.get_attribute(a)
				for prt in atb.all_probability():
					if not prt.cls in clss:
						clss[c] = 0
					clss[prt.cls] = clss[prt.cls] + (prt.prt / atb.count)
			else:
				print 'unknown attribute: %s'%a
		return clss


if __name__ == '__main__':
	# 测试
	nbc = NaiveBayesClassifier(BaseDriver())
	test_classifer(nbc)

