# * _____________________________________________________________________
content = ""
letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


with open("./main.txt", "r", encoding="utf-8") as file:
    content = file.read().replace("\n", " ").replace("\t", " ").replace("\r", " ")


def add_dots(text: str):
    return (
        text.replace("?", "?.")
        .replace("!", "!.")
        .replace(":", ":.")
        .replace(";", ";.")
        .replace("...", "---.")
    )


def remove_dots(text: str):
    return (
        text
        .replace("---.", "...")
        .replace("?.", "?")
        .replace("!.", "!")
        .replace(":.", ":")
        .replace(";.", ";")
        
    )


sentences = []
current_sentence = ""

content = add_dots(content)
for sentence in content.split("."):
    sentence = sentence.strip()

    if not sentence: continue

    first_char = sentence.replace('(', '').replace(')', '').replace("«", "").replace("»", "")[0]
    count_words = len(sentence.split())


    if letters.index(first_char.lower().strip()) + 1 == count_words:
        sentences.append(sentence + ".")

with open("main_new.txt", "w", encoding="utf-8") as file:
    file.write(remove_dots('\n'.join(sentences)))


# * _____________________________________________________________________
cherry_letters = set("вишня")
count_special = 0

for word in content.split():

    raw_word = (
        word.replace("?", "")
        .replace(".", "")
        .replace(",", "")
        .replace("!", "")
        .replace("-", "")
        .replace(":", "")
        .replace(";", "")
        .replace('"', "")
        .replace("(", "")
        .replace(")", "")
        .replace("[", "")
        .replace("]", "")
        .replace("{", "")
        .replace("}", "")
        .replace("«", "")
        .replace("»", "")
        .replace("—", "")
        .replace(" ", "")
    )
    has_double = any(a == b for a, b in zip(raw_word, raw_word[1:]))


    same_letters = set(raw_word.lower()) == cherry_letters

    if has_double or same_letters:
        print(raw_word)
        count_special += 1

print(f"Количество специальных слов: {count_special}")


# * _____________________________________________________________________
import os

os.makedirs("./new_folder", exist_ok=True)
if os.path.exists("./main_new.txt") and not os.path.exists("./new_folder/main_new.txt"):
    os.rename("./main_new.txt", "./new_folder/main_new.txt")
elif os.path.exists("./main_new.txt") and os.path.exists("./new_folder/main_new.txt"):
    os.remove("./new_folder/main_new.txt")
    os.rename("./main_new.txt", "./new_folder/main_new.txt")
