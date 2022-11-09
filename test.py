# globals at any point gives you local definitions
import function_definitions
print("1:       ",globals())

from function_definitions import *
print("2:       ",globals())

def my_iterative_calculator():
    exponentation_num = 2
    pi = 3.1416
    
    def my_inner_calculator_func():
        input_num = 2 
        pi = 3.14
        
        def one_more_inner_calculator_func():
            nonlocal pi
            pi = 40000000
            print("3:       ",globals())
            
        one_more_inner_calculator_func()
        print("4:       ",globals())
          
    my_inner_calculator_func()   
    print("5:       ",globals())

my_iterative_calculator()


# locals at any point gives you local definitions
import function_definitions
print("1:       ",locals())

from function_definitions import *

print("2:       ",locals())

def my_iterative_calculator():
    exponentation_num = 2
    pi = 3.1416

    def my_inner_calculator_func():
        input_num = 2 
        pi = 3.14
        
        def one_more_inner_calculator_func():
            nonlocal pi
            pi = 40000000
            print("3:       ",locals())
            
        one_more_inner_calculator_func()
        print("4:       ",locals())
          
    my_inner_calculator_func()   
    print("5:       ",locals())

my_iterative_calculator()