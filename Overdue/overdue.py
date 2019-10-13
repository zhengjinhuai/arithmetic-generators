# 前缀表达式
# pre = str()
# for i in range(len(self.pre_formula)):
#     pre += str(self.pre_formula[i]) + ' '
# # 正确答案
# pre += ' ' + '= ' + str(self.root.number)
# print(pre)
# # 后缀表达式
# pos = str()
# for i in range(len(self.post_formula)):
#     pos += str(self.post_formula[i]) + ' '
# # 正确答案
# pos += ' ' + '= ' + str(self.root.number)
# print(pos)
# # 查重表达式
# print(self.post_formula)
# print(self.check_formula)
# che = str()
# for i in range(len(self.check_formula)):
#     che += str(self.check_formula[i]) + ' '
# # 正确答案
# che += ' ' + '= ' + str(self.root.number)
# print(che)


# def __hash__(self):
#     """只有定义__hash__,类的实例才可以作为哈希集得成员进行操作，即用set进行查重"""
#         return None
#
# def __eq__(self, other):
#     """定义__hash__()，必须得定义__eq__()"""
#     pass

# import random
# from fractions import Fraction
#
#
# class A:
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def show(self):
#         print(self.name, self.sex, self.age)
#
#     def __hash__(self):
#         print('hash ', hash(self.name + self.sex))
#         return hash(self.name + self.sex)
#
#     def __eq__(self, other):
#         if self.name == other.name and self.sex == other.sex:
#             return True
#         return False
#
#
# class NegativeError(Exception):
#     """自定义异常类"""
#     def __init__(self, ErrorInfo):
#         super(NegativeError, self).__init__() # 初始化父类
#         self.error_info = ErrorInfo
#
#     def __str__(self):
#         return self.error_info

