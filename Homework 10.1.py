def gen(rule, start_value, total_terms):
    current = start_value
    for term_index in range(total_terms):
        yield current
        current = rule(current)

next_value = lambda x: x + 3

for number in gen(next_value, 1, 5):
    print(number)
