a="1@qq.com"
import re
b=re.findall(r"^\d{5,11}@qq.com$",a)
if b==[]:
    print("qq邮箱号格式输入不正确,语重新输入")
else:
    print('邮l箱号输入正确')