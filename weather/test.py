import unittest

# 实例化
suite = unittest.TestSuite()
loader = unittest.TestLoader()

# 方法一：通过测试用例类进行加载
suite.addTest(loader.loadTestsFromTestCase(测试用例的类名称))     # class后面的那个值
suite.addTest(loader.loadTestsFromTestCase(测试用例的类名称))
# 通过runner，运行suite
runner = unittest.TextTestRunner()
runner.run(suite)

# 方法二：通过测试用例模板去加载
suite.addTest(loader.loadTestsFromModule(class名称或者模块名称))

# 方法三：通过路径加载
import os
path = os.path.dirname(os.path.abspath(__file__))
suite.addTest(loader.discover(path))