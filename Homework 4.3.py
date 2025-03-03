import random
examples = [
    [1, 2, 3, 4, 5, 6, 7, 9],
    [1, 1, 2, 1],
    [6, 3, 7]
]
for example in examples:
    new_list = [example[0], example[2], example[-2]]
    print("Input:", example)
    print("Output:", new_list)
