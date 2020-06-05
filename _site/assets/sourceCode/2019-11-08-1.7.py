from collections import OrderedDict

d = OrderedDict()

d['a'] = 1
d['v'] = 2


for key in d:
    print(key, d[key])