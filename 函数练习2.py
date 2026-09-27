az = 1
while az <= 5:
    def user(a, b, z):
        if z == "+":
            return a + b
        elif z == "-":
            return a - b
        elif z == "*":
            return a * b
        elif z == "/":
            return a / b


    print(user(int(input("请输入第一个值")),
               int(input("请输入输入第二个值")),
               input("请输入运算符号+-*/")))
