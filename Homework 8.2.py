def is_palindrome(phrase):
    filtered = ''
    for symbol in phrase:
        if symbol.isalnum():
            filtered += symbol.lower()
    reversed_filtered = ''
    for index in range(len(filtered) - 1, -1, -1):
        reversed_filtered += filtered[index]
    return filtered == reversed_filtered


