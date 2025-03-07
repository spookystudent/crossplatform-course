WeeksDayTranslation = dict()
WeeksDayTranslation['Monday'] = 'Понедельник'
WeeksDayTranslation['Tuesday'] = 'Вторник'
WeeksDayTranslation['Wednesday'] = 'Среда'

for Day in WeeksDayTranslation:
    print(Day + ' - это ' + WeeksDayTranslation[Day])

for Day, Value in WeeksDayTranslation.items():
    print(Day + ' - это ' + Value)