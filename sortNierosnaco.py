x = int(input('Podaj x:'))
y = int(input('Podaj y:'))-1

if y>x: # y=4>x=2
    pom=x # pom =2
    x=y+1 # x=4
    y=pom-1 #y = 1
for i in range (x,y,-1):
    print(f'{i}',end='')
print()
   