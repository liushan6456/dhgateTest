# -*- coding: utf-8 -*
import unittest
#import pytest
# from Cython.Tests import xmlrunner
# from Cython.Tests.xmlrunner import XMLTestRunner
class TestAdd(unittest.TestCase):
  def add(self,a,b):
      return a + b
  def test_list(self):
    a = self.add([1], [2])
    self.assertEqual(a,[1,2])
    print(a)

  def test_tuple(self):
    #assert add((1,), (2,)) == (1,2)
    b = self.add((1,),(2,))
    print(b)
    self.assertEqual(b,(1,2))


if __name__ == '__main__':
  unittest.main()
   #test_suit = unittest.TestSuite()  # 创建一个测试集合
   #test_suit.addTest(TestAdd("test_list"))  #测试套件中添加测试用例
   #test_suit.addTest(unittest.makeSuite(TestAdd))  # 使用makeSuite方法添加所有的测试方法
   #runner = xmlrunner.XMLTestRunner(output="report")
   #runner.run(test_suit)
   #pytest.main("test_add.py")
#   # TestAdd().test_tuple()
