#The range() function
#---------------------------------------------------

print(list(range(2,20,3)))
print(list(range(2,20)))
print(list(range(2)))

#---------------------------------------------------
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")
    
#---------------------------------------------------
    
num=1    
while(num<10):
    print(num)
    num+1
    break

num=1    
while(num<10):
    print(num)
    num+1
    continue

num=1    
while(num<10):
    print(num)
    continue
    num+1
    
num=1    
while(num<10):
    if(num<6):
     print(num)
    num+1

#---------------------------------------------------


num=1    
while(num<10):
    if(num<6):
        pass
    num+=1
    print(num)
    

num=1    
while(num<10):
    if(num<6):
        pass
    num+=1
    print(num)