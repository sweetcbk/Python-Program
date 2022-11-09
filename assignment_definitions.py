def list_display_members(members):
    """Display number of elements in the members list"""
    print("Members list = ",end = " ")
    for elem in members:
        print(elem,end= " ")

def list_add_element(members):
    """Add "Ross" to the members collection """
    members.append(input("Please input an element to add to the existing list "))
    list_display_members(members)

def list_add_elements(members):
    """Add "David","Bret","Sanju"  to the members collection"""    
    received_str = input("Please input elements comma seperated to add to the existing list ")
    members.extend(received_str.split(","))
    list_display_members(members)

def list_remove_element(members):
    """  Remove the third member from the collection"""    
    members.pop(int(input("Please enter the subscript you would want to remove element from")))
    list_display_members(members)

def remove_last_element(members):
    """Remove the last member from the collection """
    members.pop()
    list_display_members(members)    

def display_3_4_5_element(members):
    """Display third, fourth and fifth element from the collection """    
    print(members[2]+ " " + members[3]+ " " + members[4])    
    list_display_members(members)    

def my_list_store():
    print("\n Welcome to Our List Store !!! ")
    print("Please enter a list Comma seperated that you would want to perform Operation Upon")
    members = input('for ex: ["Pratiksha","Kevin","Sachin","Yuvraj","Sania"] \n').split(",")

    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("  1:  Display number of elements in the members list")
        print("  2:  Add an element to the members collection like 'Sehwag' ")
        print("  3:  Add elements to the members collection like ['David','Bret','Sanju']")
        print("  4:  Remove a member from the collection at a given subscript")
        print("  5:  Remove the last member from the collection ")
        print("  6:  Display third, fourth and fifth element from the collection ")
        print("  7: Exit the Program ")
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            list_display_members(members) 
        elif choice ==2:
            list_add_element(members) 
        elif choice ==3:
            list_add_elements(members)
        elif choice ==4:
            list_remove_element(members) 
        elif choice ==5:
            remove_last_element(members) 
        elif choice ==6:
            display_3_4_5_element(members) 
        elif choice ==7:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")
    
def dict_display_capitals(capitals):
    """Display number of elements in the capitals collection"""
    print("capitals dictionary = ",end = " ")
    for elem in capitals.items():
        print(elem,end= " ")

def dict_add_element(capitals):
    """Add "Afghanistan": "Kabul"  to the capitals collection """
    inp_key = input("Please enter the key to add ")
    inp_val = input("Please enter the value to add ")
    capitals.setdefault(inp_key,inp_val)
    dict_display_capitals(capitals)		



def dict_add_elements(capitals):
    """Add Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella to the capitals collection"""    
    """ Logic : 
    1) "key1":"val1","key2":"val2"
        2) 
        "key1":"val1" ==> list("key1", "val1") ==> capitals("key1") = "val1"
        "key2":"val2" ==> list("key2", "val2") ==>  capitals("key2") = "val2"
    """
    received_str = input("Please input dictinary elements comma seperated to add ")

    for dict_elem in received_str.split(","):
        temp_list = list(dict_elem.split(":"))
        capitals[temp_list[0].replace('"','').strip()] = temp_list[1].replace('"','').strip()
    dict_display_capitals(capitals)		
	
	
def dict_remove_element(capitals):
    """Remove the USA from the collection"""    
    capitals.pop(input("Please enter the key you would want to remove"))
    dict_display_capitals(capitals)		

def my_dict_store():
    print("\n Welcome to Our Dict Store !!! ")
    print("Please enter a list Comma seperated dictionary elements that you would want to perform Operation Upon")
	
    capitals= {}
    for dict_elem in input('for ex:  India : New Delhi , USA : Washington DC, Nepal : Kathmandu, Ukraine :  Kyiv \n').split(","):
        temp_list = list(dict_elem.split(":"))
        capitals[temp_list[0].replace('"','').strip()] = temp_list[1].replace('"','').strip()

    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("    1: Display number of elements in the capitals collection")
        print('    2: Add an element to the capitals collection like --> Afghanistan: Kabul')
        print('    3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella')
        print("    4: Remove an element from the collection 	")
        print("    5: Exit the Program ")
        
    
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            dict_display_capitals(capitals) 
        elif choice ==2:
            dict_add_element(capitals)
        elif choice ==3:
            dict_add_elements(capitals)
        elif choice ==4:
            dict_remove_element(capitals) 
        elif choice ==5:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")