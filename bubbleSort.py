while True:
 try:
    n = int(input("Enter number of elements you want to add to the list "))  
    break
 except ValueError:
    print("Wrong value!")
    continue
while True:   
 try:  
    lista=list(map(float,input("Enter numbers separated by space : ").strip().split()))[:n]  
    for i in range(n):
        for j in range(0, n-i-1): 
            if lista[j] > lista[j+1] : 
                lista[j], lista[j+1] = lista[j+1], lista[j] 
    print("Sorted in ascending order: ",lista)  
    for i in range(n):
        for j in range(0,n-i-1): 
            if lista[j] < lista[j+1] : 
                lista[j], lista[j+1] = lista[j+1], lista[j] 
    print("Sorted in descending order: ",lista)   
    break   
 except ValueError:  
    print("It is not a number, please enter only numbers!")
    continue   
w=input ("")