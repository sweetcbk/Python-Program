
num = int(input("Enter Number: "))

while True:
   
  if num%3==0:
     print("Fizz")
    
  elif num%5==0:
     print('Buzz')
 
  elif (num%3==0,num%5==0):
      print('Fizz Buzz')
      
  choice = input("Let's do Continew? (yes/no): ")
 
  if choice == "no":
    print('Thank You')
    break
   
  else:
   print('Invelid Input') 
 
    






