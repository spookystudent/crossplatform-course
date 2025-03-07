full_name = input("Введите ваше полное имя: ")
words = full_name.split()
longest_word = ""
shortest_word = words[0]
for word in words:
   if len(word) > len(longest_word):
       longest_word = word
   if len(word) < len(shortest_word):
       shortest_word = word
print(f"Самое длинное слово: {longest_word}")
print(f"Самое короткое слово: {shortest_word}")
