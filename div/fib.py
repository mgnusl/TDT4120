def fib(makslengde):
    list = []
    list.append(0)
    list.append(1)
    
    for i in range(0, makslengde):
        list.append(list[i] + list[i+1])
    return list

print fib(5)