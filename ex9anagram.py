t1 = input()
t2 = input()
flag = True
t1.replace(' ', '')
t1.replace('.', '')
t1.replace(',', '')
t1.replace('!', '')
t1.replace('?', '')

t2.replace(' ', '')
t2.replace('.', '')
t2.replace(',', '')
t2.replace('!', '')
t2.replace('?', '')
if len(t1) != len(t2):
    flag = False
else:
    for i in range(len(t1)):
        if t1[i] not in t2:
            flag = False
        if t2[i] not in t1:
            flag = False
print(flag)
