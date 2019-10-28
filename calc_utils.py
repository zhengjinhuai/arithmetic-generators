import operator
from fractions import Fraction
from calc_error import NegativeError, DifficultError


class CalculatorUtils:

    @staticmethod
    def eval_formula(op, a, b, negative=False):
        """计算简单的加减乘除, 同时抛出不符合题目要求的异常

        像计算x + y这样简单的算术，最好使用Python内置的operator。
        因为operator使用的是C写的，所以执行速度相对Python代码的快
        """
        answer = 0
        if op == "+":
            answer = operator.add(a, b)
        elif op == "-":
            if operator.lt(a, b) and negative is False:  # a是否小于b
                raise NegativeError()  # 抛出结果为负数的异常对象
            else:
                answer = operator.sub(a, b)
        elif op == "*":
            answer = operator.mul(a, b)
        elif op == "/":
            if operator.gt(b, 99):  # b是否大于99
                raise DifficultError()  # 抛出题目较难的异常对象(分母大于99)
            else:
                answer = operator.truediv(a, b)
                # 如果答案为浮点数，则转换为分数形式
                if isinstance(answer, float):
                    answer = operator.truediv(Fraction(a),  Fraction(b))
        return answer

    @staticmethod
    def get_answer(formula_list, negative):
        """计算后缀表达式的结果"""
        num_list = list()
        for formula in formula_list:
            if isinstance(formula, int) or isinstance(formula, Fraction):
                num_list.append(formula)
            else:
                b = num_list.pop()
                a = num_list.pop()
                res = CalculatorUtils.eval_formula(formula, a, b, negative)
                num_list.append(res)
        return num_list.pop()

    @staticmethod
    def grading(user_ans, ans_list):
        """评分，同时返回要求的评分输出格式"""
        correct = list()
        wrong = list()
        length = len(user_ans)
        for i, u, ans in zip(range(1, length + 1), user_ans, ans_list):
            if u == ans:
                correct.append(i)
            else:
                wrong.append(i)
        return correct, wrong
