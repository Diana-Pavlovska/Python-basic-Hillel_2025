def list(lst):
    if not lst:
        return [[], []]
    middle = (len(lst)+1) //2
    half_1 = lst[:middle]
    half_2 = lst[middle:]
    return [half_1, half_2]
print("[1,2,3,4,5,6] =>", list([1,2,3,4,5,6]))
print("[1,2,3] =>", list([1,2,3]))
print("[1,2,3,4,5] =>", list([1,2,3,4,5]))
print("[1] =>", list([1]))
print("[] =>", list([]))