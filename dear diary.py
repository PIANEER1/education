import datetime
import os
while True:
    a = input()
    if a == '☺' :
        os.remove("C:\DonRobot/new_group\PIANEER\дневник.txt")
        break
    file = open('дневник.txt', 'a', encoding= 'utf-8')
    file.write(f'{datetime.datetime.now()} {a}\n')
    file.close()
    