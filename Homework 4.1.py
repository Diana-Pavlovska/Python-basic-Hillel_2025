def zero(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == 0:
            lst.pop(i)
            lst.append(0)
    return lst
print(zero([0, 1, 0, 12, 3]))
print(zero([0]))
print(zero([1, 0, 13, 0, 0, 0, 5]))
print(zero([9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]))
