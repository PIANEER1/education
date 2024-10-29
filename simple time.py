import time 
a = int(input('введите время в секундах: '))
q = 0
import datetime

current_time = datetime.datetime.now().time()
print(f'текущее время {current_time.hour}:{current_time.minute}:{current_time.second}')
for i in range(a):
    q = q + 1
    print(f'{q} прошло секунд' )
    time.sleep(1)
if a % 3600 == 0:
    print('прошло',a // 3600,'ч')
if a % 60 == 0:
    print('прошло',a // 60,'мин',)
else:
    print(f'прошло {a} с ')

current_time = datetime.datetime.now()
print(f'текущее время {current_time.hour}:{current_time.minute}:{current_time.second}')
