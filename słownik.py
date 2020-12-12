n = int (input("Podaj ilość atrybutów:"))
l = {}
for i in range(n):
    keys = input("atrybut:")
    values = input("wartość:")
    l[keys]=values

print(l)    