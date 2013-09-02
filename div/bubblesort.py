l = [5, 3, 1, 7, 4, 9, 8]

def bubblesort(list):
    for i in range(1, len(list)):
        for j in range(0, len(list)-1):
            if list[j] > list[j + 1]:
               list[j + 1], list[j] = list[j], list[j + 1]
    return list

print bubblesort(l)
