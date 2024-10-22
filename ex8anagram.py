a = input()
b = input()
flag = True
if len(a) != len(b):
    flag = False
else:
    for i in range(len(a)):
        if a[i] not in b:
            flag = False
        # if a[i] in b:
        #     print(flag)
        if b[i] not in a:
            flag = False
print(flag)
