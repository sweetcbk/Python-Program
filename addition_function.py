#-----------------------------------------------------------

def my_addition(first_num,second_num):
   
    return first_num+ second_num


first_num = int(input("Enter First number:"))
second_num = int(input("Enter Second number:"))

returned_value = my_addition(first_num,second_num)
print("Addition of the numbers is : ",returned_value)

#------------------------------------------------------------

def my_square(first_num):
   
    return str(first_num**2)

returned_value = my_square(first_num)
print("Square of the number is :",returned_value)

#------------------------------------------------------------

def my_exponenation(first_num,second_num):
    
    return first_num**second_num

returned_value = my_exponenation(first_num,second_num)
print("Exponenation of the numbers is ",returned_value)

#--------------------------------------------------------------

def my_uppercase_func(my_string):
    my_string = str(input("Enter small latter :"))
    
   
    return my_string.upper()

returned_value = my_uppercase_func(my_string=0)
print("Exponenation of the numbers is ",returned_value)