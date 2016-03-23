prefixes = "JKLMNOPQ"
suffix_1 = 'ack'
suffix_2 = 'uack'

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter + suffix_2)
    else:
        print(letter + suffix_1)
