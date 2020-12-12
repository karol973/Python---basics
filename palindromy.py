# string = input()
#strlength= len(string)
#strsliced = string[strlength::-1]
##print (strsliced)
##if (strsliced==string):
    #print("It's palindrome")
#else:
   #  print("It's not palindrome")

def reverse(p):
    str =""
    for i in p:
        str = i+str
    return str
p = "panasonic"
print("The original string is: ",end="")
print(p)

print("The reversed string is: ",end="")
print(reverse(p))
if (p==reverse(p)):
    print("It's palindrome")
else:
     print("It's not palindrome")
