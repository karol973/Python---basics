i = 1
ilosc = int(input('Ilość wierszy: ')) +1
znak = input('Znak: ')
print()

for i in range(1, ilosc):
    print(znak * i)
    i = i + 1
print()