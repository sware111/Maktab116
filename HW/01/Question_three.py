word_one = input()
word_two = input()

split_word_one = word_one[:-1]
split_word_two = word_two[:-1]

print(split_word_two + word_one[-1] + " " + split_word_one+word_two[-1])