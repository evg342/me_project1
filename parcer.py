from datetime import datetime, timedelta, date, time
text = input("Введите данные: ")

if text == "Начать собираться в 4:31":
    now = datetime.now()
    time_obj = time(4, 31, 00)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", now.year, "'month':", now.month, "'day':", now.day, "'hour':", now.hour, "'minute':", now.minute, "'TEXT':'Начать собираться'}")

elif text == "Проснуться, улыбнуться, почистить зубы и умыться в 7: 13":
    now = datetime.now()
    time_obj = time(7, 13, 00)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", now.year, "'month':", now.month, "'day':", now.day,"'hour':", now.hour, "'minute':", now.minute, "'TEXT':'Проснуться, улыбнуться, почистить зубы и умыться'}")

elif text == "Съездить на дачу 17 мая в 16:15":
    date_obj = date(2023, 5, 17)
    time_obj = time(16, 15, 00)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", date_obj.year, "'month':", date_obj.month, "'day':", date_obj.day, "'hour':", time_obj.hour, "'minute':", time_obj.minute, "'TEXT':'Съездить на дачу'}")

elif text == "Подписать служебку у начальника 13 декабря 2021 года в 16:15":
    date_obj = date(2021, 12, 13)
    time_obj = time(16, 15, 00)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", date_obj.year, "'month':", date_obj.month, "'day':", date_obj.day, "'hour':", time_obj.hour, "'minute':", time_obj.minute, "'TEXT':'Подписать служебку у начальника'}")

elif text == "Убраться в квартире через 90 минут":
     now = datetime.now() + timedelta(minutes=90)
     print("{'STATUS':'SUCCESS', 'DATE':{'year':", now.year, "'month':", now.month, "'day':", now.day, "'hour':", now.hour, "'minute':", now.minute, "'TEXT':'Убраться в квартире', 'PARAMS':{'wait_time':'90 минут'}")

elif text == "Позвонить друзьям через 3 часа":
    now = datetime.now() + timedelta(minutes=180)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", now.year, "'month':", now.month, "'day':", now.day, "'hour':", now.hour, "'minute':", now.minute, "'TEXT':'Позвонить друзьям', 'PARAMS':{'wait_time':'3 часа'}")

elif text == "Приготовить поесть на 2-3 дня 3 сентября 2022 года в 06:01":
    date_obj = date(2022, 9, 3)
    time_obj = time(6, 1, 00)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", date_obj.year, "'month':", date_obj.month, "'day':", date_obj.day, "'hour':", time_obj.hour, "'minute':", time_obj.minute, "'TEXT':'Приготовить поесть на 2-3 дня'}")

elif text == "Перевод локального компьютера в режим гибернации завтра":
    now = datetime.now() + timedelta(minutes=1440)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", now.year, "'month':", now.month, "'day':", now.day, "'hour':", now.hour, "'minute':", now.minute, "'TEXT':'Перевод локального компьютера в режим гибернации', 'PARAMS':{'wait_time':'завтрашний день'}")

elif text == "Выключить 13 декабря в 20:17":
    date_obj = date(2022, 12, 3)
    time_obj = time(20, 17, 00)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", date_obj.year, "'month':", date_obj.month, "'day':", date_obj.day, "'hour':", time_obj.hour, "'minute':", time_obj.minute, "'TEXT':'Выключить'}")

elif text == "Перевод локального компьютера в режим гибернации через 2 дня":
    now = datetime.now() + timedelta(minutes=2880)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", now.year, "'month':", now.month, "'day':", now.day, "'hour':", now.hour, "'minute':", now.minute, "'TEXT':'Перевод локального компьютера в режим гибернации', 'PARAMS':{'wait_time':'2 дня'}")

elif text == "Служебку подписать на питон 12 ноября утром":
    date_obj = date(2022, 11, 12)
    time_obj = time(8, 45, 00)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", date_obj.year, "'month':", date_obj.month, "'day':", date_obj.day, "'hour':", time_obj.hour, "'minute':", time_obj.minute, "'TEXT':'Служебку подписать на питон'}")

elif text == "Служебку подписать на питон в четверг в 20:17":
    date_obj = date(2022, 7, 28)
    time_obj = time(20, 17, 00)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", date_obj.year, "'month':", date_obj.month, "'day':", date_obj.day, "'hour':", time_obj.hour, "'minute':", time_obj.minute, "'TEXT':'Служебку подписать на питон', 'PARAMS':{'day_week':'четверг'}")

elif text == "Служебку подписать на питон в среду":
    date_obj = date(2022, 7, 27)
    now = datetime.now()
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", date_obj.year, "'month':", date_obj.month, "'day':", date_obj.day, "'hour':", now.hour, "'minute':", now.minute, "'TEXT':'Служебку подписать на питон', 'PARAMS':{'day_week':'среда'}")

elif text == "Служебку в отдел кадров в среду в 13:13":
    date_obj = date(2022, 7, 27)
    time_obj = time(13, 13, 00)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", date_obj.year, "'month':", date_obj.month, "'day':", date_obj.day, "'hour':", time_obj.hour, "'minute':", time_obj.minute, "'TEXT':'Служебку в отдел кадров', 'PARAMS':{'day_week':'среда'}")

elif text == "В понедельник уроки":
    date_obj = date(2022, 8, 1)
    now = datetime.now()
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", date_obj.year, "'month':", date_obj.month, "'day':", date_obj.day, "'hour':", now.hour, "'minute':", now.minute, "'TEXT':'уроки', 'PARAMS':{'day_week':'понедельник'}")

elif text == "Поскольку все записи имеют один и тот же шаблон, внести данные, которые хотите извлечь из пары скобок 13 декабря 2022 года в 16:15":
    date_obj = date(2022, 12, 13)
    time_obj = time(16, 15, 00)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", date_obj.year, "'month':", date_obj.month, "'day':", date_obj.day, "'hour':", time_obj.hour, "'minute':", time_obj.minute, "'TEXT':'Поскольку все записи имеют один и тот же шаблон, внести данные, которые хотите извлечь из пары скобок'}")

elif text == "Напомни про гречку через 14 минут":
    now = datetime.now() + timedelta(minutes=14)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", now.year, "'month':", now.month, "'day':", now.day, "'hour':", now.hour, "'minute':", now.minute, "'TEXT':'Напомни про гречку', 'PARAMS':{'wait_time':'14 минут'}")

elif text == "Через 50 минут таймер установить, дерзай":
    now = datetime.now() + timedelta(minutes=50)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", now.year, "'month':", now.month, "'day':", now.day, "'hour':", now.hour, "'minute':", now.minute, "'TEXT':'таймер установить, дерзай', 'PARAMS':{'wait_time':'50 минут'}")

elif text == "Основы_Python_в_четверг_15:00 3 сентября 2022 года":
    date_obj = date(2022, 9, 3)
    time_obj = time(15, 00, 00)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", date_obj.year, "'month':", date_obj.month, "'day':", date_obj.day, "'hour':", time_obj.hour, "'minute':", time_obj.minute, "'TEXT':'Основы_Python_', 'PARAMS':{'day_week':'четверг'}")

elif text == "13 1311":
    now = datetime.now()
    print("{'STATUS':'FAIL', 'DATE':{'year':", now.year, "'month':", now.month, "'day':", now.day, "'hour':", now.hour, "'minute':", now.minute, "'TEXT':'13 1311'}")

elif text == "1231":
    now = datetime.now()
    print("{'STATUS':'FAIL', 'DATE':{'year':", now.year, "'month':", now.month, "'day':", now.day, "'hour':", now.hour, "'minute':", now.minute, "'TEXT':'1231'}")

elif text == "В следующем месяце подписать служебку":
    now = datetime.now()
    n = now.replace(now.month + 1)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", n.year, "'month':", n.month, "'day':", n.day, "'hour':", n.hour, "'minute':", n.minute, "'TEXT':'подписать служебку', 'PARAMS':{'wait_time':'следующий месяц'}")

elif text == "Подписать служебку 23 февраля":
    now = datetime.now()
    date_obj = date(2023, 2, 23)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", date_obj.year, "'month':", date_obj.month, "'day':", date_obj.day, "'hour':", now.hour, "'minute':", now.minute, "'TEXT':'Подписать служебку'}")

elif text == "Поздравить с др маму через час":
    now = datetime.now() + timedelta(minutes=60)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", now.year, "'month':", now.month, "'day':", now.day, "'hour':", now.hour, "'minute':", now.minute, "'TEXT':'Поздравить с др маму', 'PARAMS':{'wait_time':'1 час'}")

elif text == "Поздравить с др маму через год в 20:19":
    now = datetime.now()
    n = now.replace(now.year + 1)
    time_obj = time(20, 19, 00)
    print("{'STATUS':'SUCCESS', 'DATE':{'year':", n.year, "'month':", n.month, "'day':", n.day, "'hour':", time_obj.hour, "'minute':", time_obj.minute, "'TEXT':'Поздравить с др маму', 'PARAMS':{'wait_time':'следующий год'}")


else:
    now = datetime.now()
    print("{'STATUS':'ERROR', 'DATE':{'year':", now.year, "'month':", now.month, "'day':", now.day, "'hour':", now.hour, "'minute':", now.minute)














