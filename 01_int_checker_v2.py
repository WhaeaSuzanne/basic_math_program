'''
component 1 - integer checker function
v1 - checking to see that the function is called, returns a value
v2 - use a try and except to check its an integer, return the integer, otherwise keep looping until the user enters an integer
'''

def int_checker(question, error_message):
    x = True
    while x == True:

        try:
            int_num = int(input(question))
            x = False
        except:
            print(error_message)

    return(int_num)

#main
#check that the int checker is called and returns a number

returned_num = int_checker("Please enter an integer: ", "This is not an integer - please enter an integer: ")
print(returned_num)
