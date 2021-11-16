#To Calculate the even index of a string
#Solve-1
String = input("Enter the String: ")
size = len(String)
def even_indx(String):
    for i in range(0,size-1,2):
        print("Index number :",i," ",String[i])
print(even_indx(String))
#Solve-2
String = input("Enter the String: ")
inputString = list(String)
for i in inputString[0::2]:
    print(i)
#Problem-3: Remove any of the first character from a string
#solve-1
input_string=input("Enter the String : ")
input_int =int(input("Enter the number of string to remove : "))
def character_remove(input_string,input_int):
    print("This is the main string ",input_string)
    slice_method=input_string[input_int:]
    return slice_method
print("remove first character")
print(character_remove(input_string,input_int))