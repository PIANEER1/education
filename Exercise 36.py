# 1 и 2 года собаки = 10,5 лет человека 
# 3;4;5;6....... = + 4 года человека 

age = int(input())
a = 0
if age == 1:
    print(10.5)
if age == 2:
    print(10.5)
if age > 2:
    a = age - 2
    a = a * 4 
    a = a + 10.5
    print(a)