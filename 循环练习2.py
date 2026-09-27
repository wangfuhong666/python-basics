password = 6895  # 把密码存在password里
index = 0  # index为用户输入次数

while index < 5:  # 如果用户输入次数<5且密码错误则继续这个循环
    a = int(input("请输入密码(四位数)"))  # 让用户输入密码并转为整数类型
    index = index + 1  # 并使用户输入次数+1
    if password == a:  # 如果密码整得等于用户输入的密码
        print("密码正确")  # 则打印密码正确
        break  # 并终止循环
    else:  # 否则
        print("密码错误,还剩的次数", 5 - index)  # 就打印这句话,并继续循环
        if index == 5:  # 当用户输入的次数真的等于5次后,停止循环(条件不满足)
            print("你已经输错五次账号将永久封禁")  # 就打印这句话
