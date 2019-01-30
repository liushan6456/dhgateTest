# -*- coding: utf-8 -*
import unittest
import pytest
# from Cython.Tests import xmlrunner
# from Cython.Tests.xmlrunner import XMLTestRunner

def add(a, b):
  return a + b

def test_str():
  '''
  测试字符串
  :return:
  '''
  # 测试失败
  assert add('1', '2') == '112'

def test_int():
  '''
  测试整型
  :return:
  '''
  assert add(1, 2) == 3


class TestAdd(unittest.TestCase):
  def test_list(self):
    assert add([1], [2]) == [1,2]
    print(add([1], [2]))

  def test_tuple(self):
    print(add((1,), (2,)))
    assert add((1,), (2,)) == (1,2)


if __name__ == '__main__':
#   test_suit = unittest.TestSuite()  # 创建一个测试集合
#   # test_suit.addTest(TestAdd("test_list"))  #测试套件中添加测试用例
#   test_suit.addTest(unittest.makeSuite(TestAdd))  # 使用makeSuite方法添加所有的测试方法
#   runner = xmlrunner.XMLTestRunner(output="report")
#   runner.run(test_suit)
    pytest.main("-s test_add.py")
#   # TestAdd().test_tuple()
