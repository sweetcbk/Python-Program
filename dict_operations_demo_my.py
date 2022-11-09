
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
my_dict = {'name': 'Chandra Bhushan', 'age': 25}
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)


#---------------------------------------------------
# Changing and adding Dictionary Elements
#---------------------------------------------------


my_dict['age'] = 26
print(my_dict)

my_dict['address'] = 'Patna'
print(my_dict)



#---------------------------------------------------
# remove a particular item, returns its value
#---------------------------------------------------

print(squares.pop(3))
print(squares)


#---------------------------------------------------
# remove an arbitrary item, return (key,value)
#---------------------------------------------------


print(squares.popitem())
print(squares)


#---------------------------------------------------
# remove all items
#---------------------------------------------------

squares.clear()
print(squares)

# delete the dictionary itself


#---------------------------------------------------
# Dictionary Methods
#---------------------------------------------------


print(marks)
for item in marks.items():
    print(item)
print(list(sorted(marks.keys())))


squares = {}
for x in range(6):
    squares[x] = x*x
print(squares)



#---------------------------------------------------
# Dictionary Membership Test
#---------------------------------------------------

print(1 in squares)
print(2 not in squares)
print(25 in squares)


#---------------------------------------------------
# Iterating through a Dictionary
#---------------------------------------------------

for i in squares:
    print(squares[5])