words = ["I", "love", "Python"]
sentence = ""
for word in words:
    # sentence = sentence + word + " "
    # sentence += word + " "
    sentence = " ".join(words)
print(sentence)

more_words = ["Spam", "is", "tasty!"]
print(''.join(more_words))

other_words = ("Are", 'tuples', 'iterable?')
print(' '.join(other_words))

the_meaning_of_life = [42, "is", "the", "answer"]
print(' '.join(map(str, the_meaning_of_life)))

print(", ".join("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

whose_line_is_it_anyway = ["That's", "my", "line!"]
print('\n'.join(whose_line_is_it_anyway))

numbers = ["1", "2", "3"]
print(' * '.join(numbers))