print('i am in second module')


import my_first_module                                                    #import everything
#from my_first_module importmy-name                                       #import single function
print('my_name in first module is ::', my_first_module.my_name)
print('my_list in first module is ::', my_first_module.my_list)