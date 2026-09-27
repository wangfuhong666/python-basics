a = "1 11aa8aaaiii星尘传说@的 8999868"
import re

print(re.findall("8", a))
print(re.search('1', a).span())
print(re.findall('aaa|8', a))
