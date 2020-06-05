from collections import defaultdict

d = defaultdict(list)

d['a'].append(1)

d['a'].append(2)



e = defaultdict(set)

e['a'].add(1)
e['a'].add(2)

print(d) # defaultdict(<class 'list'>, {'a': [1, 2]})
print(e) # defaultdict(<class 'set'>, {'a': {1, 2}})



