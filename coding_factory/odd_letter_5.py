words = ["apple", "banana", "cherry", "fig", "melon"]

def filter_words(words):
    return list(filter(lambda x: len(x) > 5, words))

words_bigger_5letters = filter_words(words)

print(words_bigger_5letters)

