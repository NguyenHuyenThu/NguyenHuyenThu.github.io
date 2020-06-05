myList = [1,2,4,-1,-5,3,7,-3]

data = [item for item in myList if item > 0]


pos = (n for n in myList if n > 0)

# for item in pos:
#    print(item)


values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
    

ivals = list( filter(is_int, values) )

print(ivals)