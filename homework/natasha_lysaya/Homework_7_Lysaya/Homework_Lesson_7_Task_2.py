words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def print_words(words):
    for word, count in words.items():
        print(word * count)


print_words(words)
