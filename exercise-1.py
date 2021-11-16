#To Calculate the even index of a string
#Solve-1
String = input("Enter the String: ")
size = len(String)
def even_indx(String):
    for i in range(0,size-1,2):
        print("Index number :",i," ",String[i])
print(even_indx(String))
# #Solve-2
# String = input("Enter the String: ")
# inputString = list(String)
# for i in inputString[0::2]:
#     print(i)
    
# #Problem-2: Remove any of the first character from a string
# #solve-1
input_string=input("Enter the String : ")
input_int =int(input("Enter the number of string to remove : "))
def character_remove(input_string,input_int):
    print("This is the main string ",input_string)
    slice_method=input_string[input_int:]
    return slice_method
print("remove first character")
print(character_remove(input_string,input_int))

#problem-3: check the first and last number of the list matches or not
#solve-1
def check_first_last_num(number_list):
    print("This is the given numbers: ",number_list)
    first_numb = number_list[0]
    last_numb= number_list[-1]
    while first_numb == last_numb:
        return True
    else:
        return False
        
list1 = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    element = int(input("enter numbers into list: "))
    list1.append(element) # adding the element in the empty list1[]
list_as_input=list1
print("Answer is ",check_first_last_num(list_as_input))