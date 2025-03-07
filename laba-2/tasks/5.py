lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

max_index = lst.index(max(lst))
min_index = lst.index(min(lst))

lst[max_index], lst[min_index] = lst[min_index], lst[max_index]

repeated_elements = {element: lst.count(element) for element in lst if lst.count(element) > 1}

print(f"Измененный список: {lst}")
print(f"Количество повторяющихся элементов: {repeated_elements}")
