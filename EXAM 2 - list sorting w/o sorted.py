

def read_file_words(filename):
    word_list = []
    with open(filename) as file:
        for line in file:
            word_list.append(line.strip())
    return word_list

words = read_file_words('words.txt')

print(words)
