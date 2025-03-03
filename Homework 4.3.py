import random
examples = [
    [1, 2, 3, 4, 5, 6, 7, 9],
    [1, 1, 2, 1],
    [6, 3, 7]
]
for example in examples:
    new_list1 = [example[0], example[2], example[-2]]
    print("Input:", example)
    print("Output:", new_list1)
#add random lists
random_list = [random.randint(1, 100) for option in range(random.randint(3, 10))]
new_list2 = [random_list[0], random_list[2], random_list[-2]]
print("Random:", random_list)
print("Result:", new_list2)