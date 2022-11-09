
def add(x, y):
    return x + y

def square(x, y):
    return x * 2

def exponenation(x, y):
    return x * y

print("Select operation.")
print("1.Add")
print("2.Square")
print("3.Exponenation")

while True:
   
    choice = input("Enter choice(1/2/3): ")

    if choice in ('1', '2', '3'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", square(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", exponenation(num1, num2))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
        

