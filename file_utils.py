# import time


class FileUtils:

    @staticmethod
    def write_file(expr_set, ans_set, expr_file, ans_file):
        print("正在保存题目......")
        """将生成的运算式和答案分别写进两个文件"""
        index = 0
        with open(expr_file, 'w+', encoding='utf-8') as ef:
            ef.write('题号\n')
            for content in expr_set:
                index += 1
                ef.write(str(index) + '.  ' + content + '\n')

        index = 0
        # start = time.clock()
        with open(ans_file, 'w+', encoding='utf-8') as af:
            af.write('题号    ' + '答案' + '           ' + '四则运算式子\n')
            for ans, content in zip(ans_set, expr_set):
                index += 1
                af.write("{:<5d}".format(index) + '    ' + format(str(ans), '*<8') + '      ' + content + '\n')
        # end = time.clock()
        # print('时间：', str(end - start))
        print("保存成功！")

    @staticmethod
    def write_grade_file(grade_file, correct, wrong):
        """将评分结果写进文件"""
        print("正在保存答题情况......")
        with open(grade_file, 'w+', encoding='utf-8') as gf:
            gf.write("温馨提示：Correct/Wrong后面的数字表示对/错的题目的数量，括号[]内的是对/错题目的编号\n")
            gf.write("{:<9}".format("Correct:") + str(len(correct)) + str(correct) + '\n')
            gf.write("{:<9}".format("Wrong:") + str(len(wrong)) + str(wrong) + '\n')
        print("保存成功！")
