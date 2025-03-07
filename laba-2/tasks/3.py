full_name = input("Введите ваше полное имя: ")
words = full_name.split()
sorted_words = sorted(words, key=len)
print(" ".join(sorted_words))
