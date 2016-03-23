def find(word, letter, starting_index = 0):
    index = starting_index
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find('maniana', 'i', 1))
print(find('maniana', 'i', 3))
print(find('maniana', 'i', 4))
