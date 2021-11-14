#To Calculate the even index of a string
#Solve-1
String = input("Enter the String: ")
size = len(String)
def even_indx(String):
    for i in range(0,size-1,2):
        print("Index number :",i," ",String[i])
print(even_indx(String))
#Solve-2
#String = input("Enter the String: ")
#inputString = list(String)
#for i in inputString[0::2]:
#    print(i)
 