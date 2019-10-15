import unittest
from expr_tree import Tree
from format_utils import FormatUtils


class TestMethod(unittest.TestCase):
    """单元测试类"""
    def setUp(self):
        """测试夹具，用来初始化变量"""
        self.source_expr = [1, '+', 2, '+', 3]  # 1 + 2 + 3
        self.target_expr = ['(', 1, '+', 2, ')', '+', 3]  # (1+2)+3

    def test_result(self):
        """测试查重方法是否正确"""
        self.postfix_formula1 = FormatUtils.get_result_formula(self.source_expr)  # 转换成后缀表达式
        self.postfix_formula2 = FormatUtils.get_result_formula(self.target_expr)
        self.check_formula1 = FormatUtils.get_check_formula(self.postfix_formula1)  # 转换成查重表达式
        self.check_formula2 = FormatUtils.get_check_formula(self.postfix_formula2)
        self.assertEqual(True, Tree.duplicate_check(self.check_formula1, [self.check_formula2]), """查重失败""")


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    tests = [TestMethod('test_result')]
    test_suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)

