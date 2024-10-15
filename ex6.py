roblox = input('введите роблокс: ').split()
udalila = {}

for slovo in roblox:
    if slovo in udalila:
        udalila[slovo] = udalila.get(slovo) + 1
    if slovo not in udalila:
        udalila[slovo] = 1

print(udalila)