colors = {
    "red": "красный",
    "blue": "синий",
    "green": "зеленый",
    "yellow": "желтый",
    "black": "черный",
}

print(colors)
print(list(colors.values())[-1])
del colors["red"]
print(colors)
