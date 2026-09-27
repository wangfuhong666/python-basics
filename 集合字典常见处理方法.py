a = {111, '安设开门', 333.25, True, (111, 222, 333)}
print(a)
b = {
    "1": "777",
    "2": '888',
    "3": [111, 222, 333]
}
a.add('cc')
print(a)
a.remove(111)
print(a)
c = {333, 8765, 9, False}
a.update(c)
print(a)
b.setdefault("5", 1)
print(b)
b.pop("1")
print(b)
b.popitem()
print(b)
e = {
    "9": 222
}
b.update(e)
print(b)
print(b.get("2"))
print(b.keys())
print(b.values())
print(b.items())

[111, 222]  # 列表

(111, 222)  # 元组

{111, 222}  # 集合

{
    '111': 111,
    "222": 222
}  # 字典

{
    'user-agent': '111',
    'referer': '222'
}
