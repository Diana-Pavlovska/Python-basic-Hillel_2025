entered_line = input()
words = [word.capitalize() for word in entered_line.split() if word.isalnum()]
hashtag = "#" + "".join(words)
print(hashtag[:140])
