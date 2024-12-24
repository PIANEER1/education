import datetime
import text
# чтение__________________________________________________________________
def read():
    file = open('my_diary.txt', "r", encoding="UTF-8")
    print(file.read())
    file.close()
# запись___________________________________________________________________
def write():
    file = open('my_diary.txt',"a", encoding="UTF-8")
    text_user = input(text.TEXT_WRITE_INPUT )
    today = datetime.datetime.now()
    today = today.strftime("%d.%m.%Y %H-%M-%S")
    file.write(f'{today} --> {text_user}\n')
    file.close()
# напоминание_______________________________________________________________
def alarm_write():
    file = open('C:/DonRobot/new_group/PIANEER/DIARY/my_diary_alarm.txt', "a", encoding="UTF-8")
    date = input(text.DATE_WRITE_INPUT)
    text_user = input(text.TEXT_WRITE_INPUT)
    file.write(f'{date} 00:00:00 --> {text_user}\n')
    file.close()
    
def command():
    """
    команды для записи/чтения дневник.
    """
    command = input(text.TEXT_INPUT)
    match command:
        case 'w': write()
        case 'r': read()
        case 'a': alarm_write()
        case '☺': exit()
        case _: print(text.TEXT_NOT_FOUND)

def main():
    while True:
        command()


if __name__ == '__main__':
    main()