import string
letters = string.ascii_letters
a, b = input().split('-')
start, end = letters.index(a), letters.index(b)
print(letters[start:end+1])
