def show(name):
    print(f'Przed modyfikacją: {name}')
    # print('Przed modyfikacją:',name)
    name[0] = 'Beata'
    name[1] = 'Barbara'
    name[2] = 'Bogdan'
    print(f'Po modyfikacji: {name}')
    print(f'Po modyfikacji: {id(name)}')

data = ['Anna', 'Agnieszka', 'Andrzej']

print(f'Przed wywołaniem funkcji show: {data}')
print(f'Id obiektu: {id(data)}')

show(data)

print(f'Po wywołaniu funkcji show: {data}')
data1 = {
    0:'Andrzej',
    1:"Karol"
}
print(f'\n Przed wywołaniem funkcji show: {data1}')
show(data1)