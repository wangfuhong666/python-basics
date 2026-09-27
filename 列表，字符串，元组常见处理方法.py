a = [222, 333, 444, 'jjj']
print(a)
a.append('ppp')
print(a)
a.insert(2, 555)
print(a)
b = [1, 2, '好好学习', 9]
a.extend(b)
print(a)
a.pop()
print(a)
a.remove(444)
print(a)
a.clear()
print(a)
c = ['计算机', '电子信息', '机械', ]
a.extend(c)
print(a)
a[2] = '自动化'
print(a)
print(a.index('电子信息'))
d = ['计算机', '环境', '车辆']
a.extend(d)
print(a)
print(a.count('计算机'))
aaa = a.copy()
print(aaa)
a.reverse()
print(a)
e = [99, 66, 589, 365.3, 0.235, -123, 896543]
print(e)
e.sort()
print(e)
e.sort(reverse=True)
print(e)

# a if 1else b
# 1?a:b


r = ' HelloP6561666896824655968798个会客服加密货币看 '
print(r)
print(r.replace('个', '嘞'))
print(r)
print(r.upper())
print(r.lower())
p = r.strip()
print(p)
print(p.count('l'))
print(p.find('货'))
print(r.find('货'))
print(p.find('3'))
print(p.index('个'))
g = (1, 666, '中国', 'bjg', '美国', 1)
print(g.count(1))
print(g.index(666))
print(len(g))

name = "wfh"
age = '19'
c = "我很帅"
print(name + age)
a = 10
b = 30
print(a + b)
aa = ['2025', '2', '22']
aa = '/'.join(aa)
print(aa)
print("我叫{}，{}".format(name, c))
print(f"我叫{name}，{c}")

h = (555, 'ppp', 'ooo', 999)
print(g + h)
print(g * 4)
l = (1, 66, 3.25, 8.66, 7.99)
print(max(l))
print(min(l))
print(tuple(l))
