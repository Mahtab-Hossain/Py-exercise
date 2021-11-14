#To Calculate the even index of a string
#Solve-1
String = input("Enter the String: ")
size = len(String)
for i in range(0,size-1,2):
    print("Index number :",i," ",String[i])
#Solve-2
String = input("Enter the String: ")
inputString = list(String)
for i in inputString[0::2]:
    print(i)
 