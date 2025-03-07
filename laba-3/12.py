cities = tuple([input() for i in range(5)])

if 'москва' not in [i.lower() for i in cities]:
    cities = cities + ('Москва',)

print(cities)
