# -*- coding: UTF-8 -*

import unittest
from datamining import funs
class JiebaTest(unittest.TestCase):
    def cut(self, snt):
        words = funs.cut(snt)
        print '/'.join(words)
    def test1(self):
        self.cut("电脑修好了")
        self.cut("做好了这件事情就一了百了了")


if __name__ =='__main__':  
    unittest.main()