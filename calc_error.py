class NegativeError(Exception):
    """自定义表达式不为负数的异常类"""
    def __init__(self):
        super(NegativeError, self).__init__()  # 初始化父类

    def __str__(self):
        return


class DifficultError(Exception):
    """自定义分母不能超过某个值的异常类"""
    def __init__(self):
        super(DifficultError, self).__init__()  # 初始化父类

    def __str__(self):
        return


class DuplicateError(Exception):
    """自定义异常类"""
    def __init__(self):
        super(DuplicateError, self).__init__()  # 初始化父类

    def __str__(self):
        return
