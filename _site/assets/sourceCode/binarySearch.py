def BinarySearch(array, query):
    i, j = 0, len(array) -1

    while i <=  j:
        middle = (i + j) // 2
        print('middle = ', middle)
        value = array[middle]
        print('value = ', value)
        if query == value:
            return middle
        elif query < value:
            j = middle - 1
        else:
            i = middle + 1
    return None

ar = [1,2,3,4,5,6,7]

print(BinarySearch(ar, 5))