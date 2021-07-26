import random
chisla=[random.randint(0,99) for i in range(99)]
print(chisla);
#Смотрим какие числа есть, и пишем на какие хотим изменить
a = int(input("Что будем изменять?: "))
b = int(input("На что меняем?: "))
for c in range(len(chisla)):
    if chisla[c] == a:
        chisla[c] = b
print(chisla)
