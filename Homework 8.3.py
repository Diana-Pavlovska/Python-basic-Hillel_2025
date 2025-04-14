def find_unique_value(data):
    counts = {}
    for item in data:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    for value in counts:
        if counts[value] == 1:
            return value
