def sum_index(lst):
    return sum(lst[::2]) * lst[-1] if lst else 0
print(sum_index([1, 3, 5]))
print(sum_index([6]))
print(sum_index([]))
