flag = 'y'
capitals = {"India" : "New Delhi", "USA" : "Washington DC","Nepal": "Kathmandu","Ukraine" : "Kyiv"}




flag1 = 'y'

print ("""
       1. Display number of elements in the capitals collection
       2. Add {"Afghanistan": "Kabul"}  to the capitals collection 
       3. Add "{"Albania":"Tirana","Algeria":"Algiers","Andorra":"Andorra la Vella"} to the capitals collection 
       4. Remove the USA from the collection
       Press any other key for exist
       """)


while (flag1 =='Y' or flag1 =='y'):    
    choice = (input('Enter your Choice-->(1/2/3/4):'))
    

    if (choice == '1'):
        print(capitals)
        continue
   
        
    elif (choice == '2'):
        capitals.update ({"Afghanistan":"Kabul"})
        print (f"Updated ,{capitals}")
        continue
    
    elif (choice == '3'):
        capitals.update ({"Albania":"Tirana","Algeria":"Algiers","Andorra":"Andorra la Vella"})
        print (f"Updated ,{capitals}")
        continue
        
    elif (choice == '4'):
        print(f"USA :",capitals["USA"])
        del capitals["USA"]
        print(f"Removed USA from the collection: {capitals}")
        continue
    
    
    else:
        print("----------:: PROGRAM EXITED ::--------------")
        break
    



