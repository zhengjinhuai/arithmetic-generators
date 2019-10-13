from fractions import Fraction
from calc_error import NegativeError, DifficultError


class CalculatorUtils:

    @staticmethod
    def eval_formula(operator, a, b, negative=False):
        """计算简单的加减乘除, 同时抛出不符合题目要求的异常"""
        answer = 0
        if operator == "+":
            answer = a + b
        elif operator == "-":
            if a < b and negative is False:
                raise NegativeError()  # 抛出结果为负数的异常对象
            else:
                answer = a - b
        elif operator == "*":
            answer = a * b
        elif operator == "/":
            if b > 99:
                raise DifficultError()  # 抛出题目较难的异常对象(分母大于100)
            else:
                answer = a / b
        return answer

    @staticmethod
    def get_answer(formula_list, negative):
        """计算后缀表达式的结果"""
        num_list = list()
        for i in range(len(formula_list)):
            if isinstance(formula_list[i], Fraction):
                num_list.append(formula_list[i])
            else:
                b = num_list.pop()
                a = num_list.pop()
                res = CalculatorUtils.eval_formula(formula_list[i], a, b, negative)
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
