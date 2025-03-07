WeeksDayTranslation = dict()
WeeksDayTranslation['Monday'] = 'Понедельник'
WeeksDayTranslation['Tuesday'] = 'Вторник'
WeeksDayTranslation['Wednesday'] = 'Среда'

WeeksDay = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
Day = 'Monday'


if Day in WeeksDayTranslation:
    del WeeksDayTranslation[Day]

try:
    del WeeksDayTranslation[Day]

except KeyError:
    print(Day + ' не найден')
print(WeeksDayTranslation)