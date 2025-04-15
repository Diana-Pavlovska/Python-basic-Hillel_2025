def popular_words(text, words):
    text = text.lower().split()
    return {word: text.count(word) for word in words}

sample = 'Cats chase mice'

print(popular_words(sample, ['cats', 'mice', 'dogs']))
