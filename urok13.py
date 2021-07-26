import random;

namber1 = {random.randint(1, 15) for i in range(10)}
namber2 = {random.randint(1, 31) for j in range(10)}
print(namber1)
print(namber2)
# Сумма namber1 и namber2
namber3 = namber1.copy()
namber3.update(namber2)
print(namber3)
