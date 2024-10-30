son = int(input("Sonni kiriting: "))
for i in range(son, 0, -1):
    print(i, end=", " if i > 1 else "")
son = int(input("Sonni kiriting: "))
faktorial = 1
i = 1

while i <= son:
    faktorial *= i
    i += 1

print(faktorial)  
son = input("Istalgan sonni kiriting: ")
yigindi = 0

for raqam in son:
    yigindi += int(raqam)

print(yigindi)  
ism = input("Ismingizni kiriting: ")
i = 0

while i < len(ism):
    print(ism[i])
    i += 1
