def add_one(digits):
    number = 0
    for digit in digits:
        number = number * 10 + digit
    number += 1
    result = []
    for char in str(number):
        result.append(int(char))
    return result
