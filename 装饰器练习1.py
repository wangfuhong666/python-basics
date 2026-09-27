class a:
    def __init__(self):
        print(1)
print(a().__dict__)
def decorator(func):

    def wrapper():
        print("函数开始执行")

        func()

        print("函数执行完毕")
        print()

    return wrapper
def hello():
    print("hello")
@decorator#fun=decorator(fun)
def fun():
    print("fun")
decorator(fun)()
hello = decorator(hello)
hello()
def de(*args,**kwargs):
    def tmp(func):
        def wrapper(*qargs,**qkwargs):
            print("函数开始执行")
            func(*args,**kwargs)
            print(*qargs,**qkwargs)
            print("函数执行完毕")

        return wrapper
    return tmp
@de(1,2,3)
def fun(*args,**kwargs):
    print(*args,**kwargs)
    print("fun")
fun(1,2)