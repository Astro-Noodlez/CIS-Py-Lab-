

def read_file_words(filename):
    word_list = []
    with open(filename) as file:
        for line in file:
            word_list.append(line.strip())
    return word_list

words = read_file_words('words.txt')


# print(words)

def list_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(n-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

sorts = list_sort(words)
# print(list_sort(words))

def sorted(file, list):
    with open(file, 'w') as file:
        for word in list:
            file.write(word + '\n')

filed = sorted('sorted list', sorts)

print(filed)