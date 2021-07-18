Number = float (input("Please Enter any Number: "))
suma = 0
mult = 1
while Number > 0:
    digit = Number % 10
    suma = suma + digit
    mult = mult * digit
    Number = Number // 10
print("Сумма:", suma)
#print("Умножение:", mult)