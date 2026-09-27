a = input("请输入你的手机号并按下回车")
import re

b = re.findall(r"^1[3-9]\d{9}$", a)
c = 0
while c <= 5:
    if b == []:
        print("手机号格式输入不正确")
        a = input("请输入你的手机号并按下回车")
        b = re.findall(r"^1[3-9]\d{9}$", a)
    else:
        print("手机号输入正确，请继续下一步")
        break
