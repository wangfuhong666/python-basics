def ppp():
    print("成员方法执行成功")


def pp(x, y):
    return (x * y - x - y) ^ y


class a:
    # 成员变量
    aa = None
    bb = None
    c__ = None
    long = None
    num1 = None
    num2 = None

    # 成员方法
    def b(self):
        ppp()
        print(pp(self.num1, self.num2))
        print(self.aa)
        print(self.bb)
        print(self.c__)
        print(self.long)


bbb = a()
bbb.aa = "nnnbbbb"
bbb.bb = "ffffff"
bbb.c__ = "cccccc"
bbb.num1 = 556
bbb.num2 = 888


# bbb.b()


class q:
    def __init__(self):
        self.num1 = None
        self.num2 = None

    def bbb(self):
        ppp()
        print(pp(self.num1, self.num2))


ccc = q()
ccc.bbb()
