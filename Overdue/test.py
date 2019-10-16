import time
import random
# import fractions
from fractions import Fraction


if __name__ == '__main__':
    # a = 'Is Chicago'
    # b = 'Not Chicago?'
    # start = time.perf_counter()
    # print('{} {}'.format(a, b))
    # end = time.perf_counter()
    # print("时间1：", str(end - start))
    # start = time.perf_counter()
    # print(a + ' ' + b)
    # end = time.perf_counter()
    # print("时间2：", str(end - start))
    # a = list()
    # for i in range(100):
    #     a.append(i)
    # for i, j in a:
    #     print(i,j)
    # print(random.randrange(2))
    a = random.randint(1, 9)
    b = Fraction(2,4)
    print(a-b)