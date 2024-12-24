import write_read
import datetime
import text

check = datetime.timedelta(seconds=5)

def main():
    last_time = datetime.datetime.now()
    while True:
        if datetime.datetime.now() - last_time > check:
            last_time = datetime.datetime.now()
            file = open('my_diary_alarm.txt', 'r', encoding='utf-8')
            for line in file.readlines():
                date, message = line.split('-->')
                date = datetime.datetime.strptime(date, '%d.%m.%Y %H:%M:%S ')
                print(datetime.datetime.now() - date)
                if(datetime.datetime.now() - date >= datetime.timedelta(minutes=0) and
                   datetime.datetime.now() - date >= datetime.timedelta(minutes=0, seconds=9)):
                    print(message)
                print(text.DATE_MESSAGE_PRINT.format(date=date, message=message))
            



if __name__ == '__main__':
    main()