'''
component 1 - inte checker function
v1 - checking to see that the function is called, returns a value

'''

def int_checker(min_num, max_num):
    print(min_num, max_num)
    return(min_num + max_num)

#main
#check that the int checker is called and returns a number
returned_num = int_checker(2, 45)
print(returned_num)
