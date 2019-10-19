实现一个自动生成小学四则运算题目的命令行程序
#### 程序简介
1. 自然数：0, 1, 2, …。
2. 真分数：1/2, 1/3, 2/3, 1/4, 1’1/2（等于3/2）, …。
3. 运算符：+, −, ×, ÷。
4. 括号：(, )。
5. 等号：=。
6. 分隔符：空格（用于四则运算符和等号前后）。
7. 算术表达式：
e = n | e1 + e2 | e1 − e2 | e1 × e2 | e1 ÷ e2 | (e)，其中e, e1和e2为表达式，n为自然数或真分数。

四则运算题目：e = ，其中e为算术表达式。
#### 操作说明
1. `python calc_cmd.py -r 10 -n 10`
2. -r 设置控制题目中数值（自然数、真分数和真分数分母）的范围
3. -n 设置控制生成题目的个数