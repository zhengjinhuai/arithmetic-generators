from fractions import Fraction


class FormatUtils:

    @staticmethod
    def standard_format(answer):
        """将分数转换成真分数格式，如 8/3 = 2'2/3"""
        if (answer > 1 or answer < -1) and answer.denominator != 1:
            a_numerator = answer.numerator % answer.denominator
            a_denominator = answer.denominator
            a_right = Fraction(a_numerator, a_denominator)
            a_left = answer.numerator // answer.denominator
            result = str(a_left) + '\'' + str(a_right)
        else:
            result = str(answer)
        return result

    @staticmethod
    def standard_output(formula):
        """标准的输出格式，将*转换成x /转换成÷ 分数转为真分数"""
        output = str()
        for i in range(len(formula)):
            if isinstance(formula[i], Fraction):
                # 如果为分数
                output += FormatUtils.standard_format(formula[i])
            elif isinstance(formula[i], int):
                # 如果为整型
                output += str(formula[i])
            elif formula[i] == '+':
                output += ' ＋ '
            elif formula[i] == '-':
                output += ' － '
            elif formula[i] == '*':
                output += ' × '
            elif formula[i] == '/':
                output += ' ÷ '
            else:
                output += formula[i]
        output += ' ＝ '
        return output

    @staticmethod
    def get_result_formula(formula_list):
        """将中缀表达式转换成后缀表达式"""
        op_priority = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2}
        postfix_formula = list()  # 输出后缀表达式结果
        op_list = list()
        for i in range(len(formula_list)):
            if isinstance(formula_list[i], int) or isinstance(formula_list[i], Fraction):
                # 如果为数字直接输出
                postfix_formula.append(formula_list[i])
            elif formula_list[i] == '(':
                # 如果为左括号,压栈到op_list
                op_list.append(formula_list[i])
            elif formula_list[i] == ')':
                # 如果为右括号,将op_list中所有左括号的操作符输出
                while op_list[-1] != '(':
                    postfix_formula.append(op_list.pop())
                op_list.pop()  # 将左括号出栈
            else:
                # 如果为操作符,比较该操作符和栈顶的操作符优先级作比较
                # 如果优先级大于栈顶元素压栈,否则将op_list中优先级大于或等于该操作符的元素输出
                # 最后压栈
                while len(op_list) > 0 and op_priority[op_list[-1]] >= op_priority[formula_list[i]]:
                    postfix_formula.append(op_list.pop())
                op_list.append(formula_list[i])

        while op_list:
            # 将剩余的op_list出栈
            postfix_formula.append(op_list.pop())

        return postfix_formula

    @staticmethod
    def get_check_formula(postfix_formula):
        """根据后缀表达式来生成查重表达式"""
        check_formula = list()
        temp_list = list()
        for i in range(len(postfix_formula)):
            if isinstance(postfix_formula[i], int) or isinstance(postfix_formula[i], Fraction):
                # 如果为数字压栈
                temp_list.append(postfix_formula[i])
            else:
                # 如果为操作符
                check_formula.append(postfix_formula[i])
                last = temp_list.pop()
                if last != '#':
                    check_formula.append(last)
                last = temp_list.pop()
                if last != '#':
                    check_formula.append(last)
                temp_list.append('#')
        return check_formula
