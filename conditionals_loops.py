#-----------------------------------------------------------------------
# Sum from 1 to Given number by user

num = int(input( "enter a integer: " ))
sum_num =0

if num != 0:
   for i in range(1, num+1): 
       sum_num += i
       print(sum_num)
else:
    exit()
 

#-----------------------------------------------------------------------
# sum from 1 to Given number by user

sum=1
num=int(input("Enter the Number " ))


for i in range(1, num + 1):
        sum = sum+ i
print(sum)

#------------------------------------------------------------------------
# Python program to print odd Numbers in given range


#num=int(input("Enter the Number " ))
num2=int(input("Enter the Number " ))
for num in range(1, num2 + 1):
	
	
	if num % 2 != 0:
		print(num, end = " ")


    
#---------------------------------------------------------------------
# Fibonacci sequence

n_terms = int(input ("How many terms the user wants to print? "))  
n_1 = 0  
n_2 = 1  
count = 0  
  

if n_terms <= 0:  
    print ("Please enter a positive integer, the given number is not valid")  

elif n_terms == 1:  
    print ("The Fibonacci sequence of the numbers up to", n_terms, ": ")  
    print(n_1)  

else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < n_terms:  
        print(n_1)  
        nth = n_1 + n_2  
       
        n_1 = n_2  
        n_2 = nth  
        count += 1  

#---------------------------------------------------------
# Prime Number


lower = 1
upper = int(input("Enter a Numbetr : "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

