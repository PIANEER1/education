import datetime

now = datetime.date.today()

to = datetime.datetime.now()
print(to)
if now.weekday() == 5 or now.weekday() == 6:
    print(f'сегодня выходдной ')
    
else:
    print('сегодня будний день')
    if now.weekday() == 0:
        print('пониедльник')
    if now.weekday() == 1:
        print('вторник')
    if now.weekday() == 2:
        print('среда')
    if now.weekday() == 3:
        print('четвег')
    if now.weekday() == 4:
        print('пятница')


a = input('введите: год.месяц.число ')
q = datetime.datetime.strptime(a, '%Y.%m.%d')
age = to - q
print(age)
weekday = q.weekday()
if weekday == 5 or weekday == 6:
    print(f'этот день выходдной ')
    
else:
    print('этот день будний')
    if weekday == 0:
        print('пониедльник')
    if weekday == 1:
        print('вторник')
    if weekday == 2:
        print('среда')
    if weekday== 3:
        print('четвег')
    if weekday== 4:
        print('пятница')
w = 0
while q <= to:
    q += datetime.timedelta(days=1)
    if q.weekday() == 6:
        w += 1
print(w)

