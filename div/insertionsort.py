def insertionsort(list):
    for i in range(1, len(list)):
        value = list[i]
        j = i - 1
        while j >= 0:
            if value < list[j]:
                list[j + 1] = list[j]
                list[j] = value
                j -= 1
            else:
                break
    return list
        
        
l = [5, 3, 1, 7, 4, 9, 8]
print insertionsort(l)
