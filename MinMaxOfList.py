
numberList = []
n = int(input("Enter the list size : "))

print("\n")
for i in range(1, n+1):
    print("Enter number at location", i, ":")
    item = int(input())
    numberList.append(item)
print("User List is ", numberList)
min = min(numberList)
max=max(numberList)
print ("The min is: " ,min)
print ("The max is: " ,max)