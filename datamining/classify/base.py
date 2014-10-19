#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-10-15
# @Author  : Robin (sintrb@gmail.com)
# @Link    : https://github.com/sintrb/Douban-Group-AD-Killer
# @Version : 1.0

class BaseClassifier(object):
	"""基本的分类器定义"""
	def training(self, sample, cls):
		"""使用样本训练分类器"""
		raise Exception('未实现训练方法')

	def classify(self, sample):
		"""对数据进行分类，返回该数据与各类的相似程度"""
		raise Exception('未实现分类方法')
		
	def whichclass(self, sample):
		"""对数据进行分类，返回该数据的分类"""
		clss  = self.classify(sample)
		return max(clss.items(), key=lambda x:x[1])[0]

def test_classifer(clf):
	'''
	测试分类器
	'''
	# 分类训练
	clf.training('abcdefghijklmnopqrst', 0)
	clf.training('aab', 0)
	clf.training('a', 1)
	clf.training('d', 1)
	clf.training('e', 2)
	
# 	db.show_info()

	# 分类测试
	print clf.whichclass('a')
	print clf.whichclass('c')
	print clf.whichclass('d')
	print clf.whichclass('t')
	print clf.whichclass('e')
	print clf.whichclass('opqrst')
