n = int(input())
while n > 9:
    n = eval("*".join(str(n)))
print(n)
