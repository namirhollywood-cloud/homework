word = input("Введите слово: ")
length = len(word)
if length % 2 == 0:
    middle_left = length // 2 - 1
    middle_right = length // 2 + 1
    print(word[middle_left:middle_right])
else:
    middle = length // 2
    print(word[middle])