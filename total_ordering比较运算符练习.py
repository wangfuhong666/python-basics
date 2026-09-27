import functools
@functools.total_ordering
class A:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x

    # 新增小于比较，装饰器自动补齐 > <= >=

    def __lt__(self, other):
        return self.x < other.x


a = A(10)
b = A(20)
# 调用方式1：运算符简写
print(a >= b)
# 调用方式2：魔术方法传参调用
print(a.__lt__(b))