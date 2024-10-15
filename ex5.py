dict1 = {'яблоки': 100, 'бананы': 333, 'груши': 200,
         'апельсины': 300, 'ананасы': 45, 'лимоны': 98,
     	'сливы': 76, 'манго': 34, 'виноград': 90, 'лаймы': 230}
dict2 = {'яблоки': 300, 'груши': 200, 'бананы': 400,
     	'малина': 777, 'ананасы': 12, 'лаймы': 123, 'черника': 111, 'арбузы': 666}
dictIwantbananas = {}
# 1. Создадим общий список по ключам
# 2. переведём список в сет
# 3. Цикл по сету (яблоки, бананы, ананасы)
# 4. добавление пары ключ значение в новый словарь
Iwantbananas = set(dict1.keys() or dict2.keys())


for i in Iwantbananas:
	dictIwantbananas[i] = dict1.get(i, 0) + dict2.get(i, 0)
print(dictIwantbananas)

# dictIwantbananas['Яблоки'] = 10