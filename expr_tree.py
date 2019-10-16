import os
import random
from fractions import Fraction
from calc_utils import CalculatorUtils
from file_utils import FileUtils
from format_utils import FormatUtils
from calc_error import NegativeError, DifficultError, DuplicateError
a = list()
b = list()
c = list()

class Node:
    """算式二叉树节点"""
    def __init__(self):
        self.type = 0  # Node的类别：{默认：0， 数字：1， 操作符：2， }
        self.operator = None  # 字符串类型
        self.number = None  # 分数类型
        self.left = None  # Node类型
        self.right = None  # Node类型
        self.op_priority = {'+': 1, '-': 1, '*': 2, '/': 2}

    def get_answer(self, negative=False):
        """根据生成的树，将左右子树的结果分别存进该结点的number中"""
        if self.type == 2:
            self.left.get_answer(negative)
            self.right.get_answer(negative)
            self.number = CalculatorUtils.eval_formula(
                self.operator, self.left.number, self.right.number, negative)
            # 测试运算过程
            # print(str(self.number) + '=' + str(self.left.number) + str(self.operator) + str(self.right.number))
        else:
            return

    def get_formula(self):
        """括号的匹配,获取前缀表达式"""
        formula = list()
        if self.type == 1:
            return [self.number]
        elif self.type == 2:
            # 左子树
            if self.left.type == 2 and \
                    self.op_priority[str(self.operator)] > self.op_priority[str(self.left.operator)]:
                formula.append('(')
                formula += self.left.get_formula()
                formula.append(')')
            else:
                formula += self.left.get_formula()

            # 中间结点
            formula.append(self.operator)

            # 右子树
            if self.right.type == 2 and \
                    self.op_priority[str(self.operator)] >= self.op_priority[str(self.right.operator)]:
                formula.append('(')
                formula += self.right.get_formula()
                formula.append(')')
            else:
                formula += self.right.get_formula()
            return formula

    # def show_node(self):
    #     """演示生成的二叉树的结构"""
    #     if self.type == 1:
    #         print(self.number)
    #     else:
    #         print(self.operator)
    #         print('左结点', end='')
    #         self.left.show_node()
    #         print('右结点', end='')
    #         self.right.show_node()


class Tree:
    """算式二叉树"""
    def __init__(self):
        self.root = Node()
        self.op_list = ["+", "-", "*", "/"]
        self.op_weight = [3, 6, 8, 10]  # 操作符随机出现的权重
        self.type_list = [1, 2]  # 整数:1, 真分数:2
        self.num_weight = [8, 2]  # 设置随机产生的数字类型(整数 分数)的权重
        self.pre_formula = list()  # 前缀表达式
        self.post_formula = list()  # 后缀表达式
        self.check_formula = list()  # 查重表达式
        self.result_formula = list()  # 符合要求的表达式
        self.formula = list()  # 格式化后的表达式
        self.answer = list()  # 格式标准化的答案

    def generate_formula(self, num_range, number, negative):
        """随机生成式子"""
        num = 0
        degree = random.randrange(3, 4)  # 随机设置操作数的个数
        while num < number:
            empty_node = [self.root]
            for _ in range(degree):
                '''生成操作符号节点'''
                node = random.choice(empty_node)
                empty_node.remove(node)
                node.operator = random.choices(self.op_list, cum_weights=self.op_weight)[0]
                # node.operator = random.choices(self.op_list)[0]
                node.type = 2

                # 每生成一个操作符号节点，生成两个空节点
                node.left = Node()
                node.right = Node()
                empty_node.append(node.left)
                empty_node.append(node.right)

            for node in empty_node:
                '''将所有空结点变为数字结点'''
                node.type = 1
                # 设置真分数的比重 1为整数 0为分数
                num_type = random.choices(self.type_list, self.num_weight)[0]
                if num_type == 1:
                    # 生成一个整数
                    node.number = random.randint(1, num_range)
                else:
                    # 生成一个真分数
                    node.number = Fraction(random.randint(1, num_range), random.randint(1, num_range))
            try:
                # self.root.show_node()  # 获取生成的二叉树结构
                self.root.get_answer(negative)  # 计算答案
                if self.root.number.denominator > 99:  # 分母超过99抛出异常
                    raise DifficultError()

                self.pre_formula = self.root.get_formula()  # 获取前缀表达式
                self.post_formula = FormatUtils.get_result_formula(self.pre_formula)  # 获取后缀表达式
                self.check_formula = FormatUtils.get_check_formula(self.post_formula)  # 获取查重表达式
                a.append(self.pre_formula)
                b.append(self.post_formula)
                c.append(self.check_formula)

                # 进行查重
                if not Tree.duplicate_check(self.check_formula, self.result_formula):
                    # 返回false 则表明没有重复
                    self.result_formula.append(self.check_formula)
                else:
                    raise DuplicateError

                output = FormatUtils.standard_output(self.pre_formula)  # 格式化前缀表达式
                if isinstance(self.root.number, Fraction):
                    answer = FormatUtils.standard_format(self.root.number)  # 格式化答案
                else:
                    answer = self.root.number
                # print(output, answer)
                self.formula.append(output)
                self.answer.append(answer)
            except ZeroDivisionError:
                # print("除数为零，删除该式子")
                continue
            except NegativeError:
                # print("出现负数，删除该式子")
                continue
            except DifficultError:
                # print("题目较难，删除该式子")
                continue
            except DuplicateError:
                # print("题目重复，删除该式子")
                continue
            else:
                num += 1
        return self.formula, self.answer

    @staticmethod
    def duplicate_check(target_expr, result_expr):
        """检查新生成的式子是否重复"""
        for i in range(len(result_expr)):
            if result_expr[i] == target_expr:
                return True
            if target_expr[0] == '+' or target_expr[0] == '*':
                temp = target_expr[1]
                target_expr[1] = target_expr[2]
                target_expr[2] = temp
                if result_expr[i] == target_expr:
                    return True
            return False
        return False


if __name__ == '__main__':
    t = Tree()
    e_file = os.path.join(os.getcwd(), 'Exercises.txt')
    a_file = os.path.join(os.getcwd(), 'Answer.txt')
    g_file = os.path.join(os.getcwd(), 'Grade.txt')
    formula_list, ans_list = t.generate_formula(10, 10, False)
    FileUtils.write_file(formula_list, ans_list, e_file, a_file)  # 保存题目文件
