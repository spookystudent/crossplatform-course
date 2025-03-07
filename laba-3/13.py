WeeksDayTranslation = dict()
WeeksDayTranslation['Monday'] = 'Понедельник'
WeeksDayTranslation['Tuesday'] = 'Вторник'
WeeksDayTranslation['Wednesday'] = 'Среда'

WeeksDay = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


for Day in WeeksDay:
    if Day in WeeksDayTranslation:
        print(Day + ' - это ' + WeeksDayTranslation[Day])
    else:
        print('Неизвестный день')

    