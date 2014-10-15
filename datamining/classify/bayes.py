#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-10-15
# @Author  : Robin (sintrb@gmail.com)
# @Link    : https://github.com/sintrb/Douban-Group-AD-Killer
# @Version : 1.0

from base import BaseClassifier

class NaiveBayesClassifier(BaseClassifier):
	"""朴素贝叶斯分类"""
	def __init__(self):
		super(NaiveBayesClassifier, self).__init__()
		self.classes = {}
		self.attributes = {}
	def training(self, sample, cls, force=False):
		if not cls in self.classes:
			self.classes[cls] = set()
		if not sample in self.classes[cls] or force:
			self.classes[cls].add(sample)
		for a in sample:
			if not a in self.attributes:
				self.attributes[a] = {'_count_':0.0}
			att = self.attributes[a]
			if not cls in att:
				att[cls] = 0
			att[cls] = att[cls] + 1.0/len(sample)	# 分解每个属性的权重
			att['_count_'] = att['_count_'] + 1
	def classify(self, sample):
		clss = {}
		for c in self.classes:
			clss[c]  = 0.0
		for a in sample:
			if a in self.attributes:
				att = self.attributes[a]
				for c, p in att.items():
					if c == '_count_':
						continue
					if not c in clss:
						clss[c] = 0
					clss[c] = clss[c] + (p / att['_count_'])
			else:
				print 'unknown attribute: %s'%a
		return clss

if __name__ == '__main__':
	# 测试
	nbc = NaiveBayesClassifier()

	# 分类训练
	nbc.training('abcdefghijklmnopqrst', 0)
	nbc.training('aab', 0)
	nbc.training('a', 1)
	nbc.training('d', 1)
	nbc.training('e', 2)

	# 分类测试
	print nbc.whichclass('ab')
	print nbc.whichclass('c')
	print nbc.whichclass('d')
	print nbc.whichclass('t')
	print nbc.whichclass('opqrst')

