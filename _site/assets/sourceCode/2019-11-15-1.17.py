prices = {
    'Omo':11,
    'Shiff':12,
    'Tired':98,
}

p1 = {key:value for key, value in prices.items() if value > 11}
 
print(p1)

iterator_res = ( (key,value) for key, value in prices.items() if value > 11)

p2 = dict(iterator_res)

print(p2)