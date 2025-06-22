"""
Word Occurrences
Estimate: 20 minutes
Actual:   44 minutes
"""
text = input("Text: ")
words = text.split()

word_count = {}
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
max_word_length = max(len(word) for word in word_count)

for word in sorted(word_count):
    print(f"{word:{max_word_length}} : {word_count[word]}")
