text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
words = text.split()
symbols = ",."
new_words = []


for word in words:
    if word[-1] in symbols:
        new_words.append(word[:-1] + 'ing' + word[-1])
    else:
        new_words.append(word + 'ing')


new_text = ' '.join(new_words)
print(new_text)
