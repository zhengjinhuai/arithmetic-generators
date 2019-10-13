import os
import sys
import argparse
from expr_tree import Tree
from file_utils import FileUtils
from calc_utils import CalculatorUtils


parser = argparse.ArgumentParser(description="四则运算")
parser.add_argument('-n', dest='number', type=int, default=1, help='number of generated questions')
parser.add_argument('-r', dest='range', type=int, default=10, help='range of values')
parser.add_argument('-e', dest='exercise', type=str, help='formula expression file')
parser.add_argument('-a', dest='answer', type=str, help='answer expression file')
parser.add_argument('-g', dest='grade', type=str, help='grade file')
parser.add_argument('-m', dest='minus', default=False, action='store_true',
                    help='produce formulas with negative numbers')
args = parser.parse_args()


if __name__ == '__main__':
    if args.range is None:
        print("请输入'-r'参数控制题目中数值（自然数、真分数和真分数分母）的范围")
    if args.exercise is None:
        args.exercise = os.path.join(os.getcwd(), 'Exercises.txt')
    if args.answer is None:
        args.answer = os.path.join(os.getcwd(), 'Answer.txt')
    if args.grade is None:
        args.grade = os.path.join(os.getcwd(), 'Grade.txt')
    print("欢迎进入答题模式......(输入'exit'可退出程序)")
    t = Tree()
    u_answer = list()  # 用户答案
    formula, s_answer = t.generate_formula(args.range, args.number, args.minus)  # 随机生成表达式
    FileUtils.write_file(formula, s_answer, args.exercise, args.answer)  # 保存题目文件
    for i in range(args.number):
        print(formula[i], end='')
        answer = input()  # 获取用户输入的答案
        if answer == 'exit':
            print('退出程序成功！')
            sys.exit()
        u_answer.append(answer)
    correct, wrong = CalculatorUtils.grading(u_answer, s_answer)  # 统计答题结果
    FileUtils.write_grade_file(args.grade, correct, wrong)  # 保存答题结果
