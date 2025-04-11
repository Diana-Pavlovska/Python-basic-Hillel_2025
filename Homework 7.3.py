def second_index(text, symbol):
    first = text.find(symbol)
    if first == -1:
        return None
    second = text.find(symbol, first + 1)
    return second if second != -1 else None
