# mesec = input('ВВЕДИТЕ ПОЖАЛУЙСТА МЕСЯЦ: ')
# match mesec:
#     case 'декабрь' : print('гдэ снег???????????')
#     case 'январь' : print('где снег аааааааавиасейлс')
#     case 'февраль' : print('дайте снег пожалуйста')
#     case 'июнь' : print('урааааа каникулы')
#     case 'июль' : print('урааааа днюха')
#     case 'август' : print('урааааа кани... НЕХОЧУ в школу')
#     case a : print(f'{a} это не mesec')


# neme = input()
# a = ''
# a = None if not bool(neme) else neme

# print(f'привет ты кто' if a == None else f'привет {neme}')



q = input().split()
match q:
    case (a,): print('1D')
    case (a,b): print('2D')
    case (a,b,c): print('3d')
    case (a,b,c,d):print('4D')
