duration = int(input('Введите промежуток времени в секундах: '))
minute = duration // 60
hour = minute // 60
day = hour // 24
month = day // 30    # условно взято 30 дней
if duration < 60:
    print(duration, 'сек')
elif duration >= 60 and duration < 3600:
    duration = duration % 60
    print(minute, 'мин', duration, 'сек')
elif duration >= 3600 and duration < 86400:
    duration = duration % 60
    minute = minute % 60
    print(hour, 'ч', minute, 'мин', duration, 'сек')
elif duration >= 86400 and duration < 2592000:
    duration = duration % 60
    minute = minute % 60
    hour = hour % 24
    print(day, 'д', hour, 'ч', minute, 'мин', duration, 'сек')
elif duration >= 2592000 and duration < 31104000:
    duration = duration % 60
    minute = minute % 60
    hour = hour % 24
    day = day % 30
    print(month, 'м', day, 'д', hour, 'ч', minute, 'мин', duration, 'сек')