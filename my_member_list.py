flag = 'y'
member_list = []
while (flag =='Y' or flag =='y'):
    members = (input('Enter the Names of Member :'))
    member_list.append(members)
    
    flag = (input("Add another Member's Names? (Y/N) :"))
    if (flag == 'Y'or flag =='y'):
        continue
    else:
        print(":: Exited from Updating Member's Name  ::")
        print(member_list)
        break
flag1 = 'y'
print ("""
       1. Display Numbers of elements in the members list
       2. Add "Ross" to the members collection
       3. Add "Dravid","Mahindra","Sanjay" to the members collection
       4. Remove the third member from the collection
       5. Remove the last member from the collection
       6. Display third, fourth and fifth element from the 
       7. Exit Program
       """)
while (flag1 =='Y' or flag1 =='y'):    
    choice = (input('Enter your Choice-->(1/2/3/4/5/6/7):'))
    

    if (choice == '1'):
        print(member_list)
        print(len(member_list))
        continue
   
        
    elif (choice == '2'):
        member_list.append("Ross")
        print(f"Updated {member_list}")
        continue
        
    elif (choice == '3'):
        member_list = member_list + ["Dravid","Mahindra","Sanja"]
        print(f"Updated {member_list}")
        continue
    
    elif (choice == '4'):
        print("Deleted Member:",member_list[3])
        del member_list[3]
        print(f"Updated {member_list}")
        continue
    
    elif (choice == '5'):
        print(member_list.pop())
        print(f"Last Member Removed: {member_list}")
        continue
    
    elif (choice == '6'):
        print(member_list[3:6]) 
        print(member_list)
        continue
    
    elif (choice == '7'):
        print("----------:: PROGRAM EXITED ::--------------")
        exit(member_list)
        
    else:
        print("-------------------------------")
        print(":: Exited Operations ::")
        break