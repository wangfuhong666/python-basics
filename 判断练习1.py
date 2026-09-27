# 1. 编写一个程序，根据学生的成绩判断其等级：
# 90分及以上：优秀
# 80到89分：良好
# 70到79分：中等
# 60到69分：及格
# 60分以下：不及格
o = 0
while o < 5:
    a = int(input("请输入你的成绩"))
    if a >= 90:
        print("优秀")
    elif a >= 80:
        print("良好")
    elif a >= 70:
        print("中等")
    elif a >= 60:
        print("及格")
    else:
        print("不及格")
