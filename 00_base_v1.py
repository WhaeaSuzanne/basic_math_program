'''
game to ask basic math questions
base component
v1 - set up the skeleton of the program, test the functions are called as required
v2 - trial random generator function component. Works well so will keep it
CC SA 2022

'''
#import library************************************************
import random as r

#set up functions**********************************************

#function to check for integers. will loop until an integer is input
def int_checker():
    print("placeholder")


#function to check string is within an allowable list. Will loop until an allowable word is input
def string_checker(list_of_allowable):
    print("placeholder")


#function to add two randomly generated numbers
def addition():
    print("addition function")

#function to subtract two randomly generated numbers
def subtraction():
    print("subtraction function")

#function to multiply two randomly generated numbers
def multiplication():
    print("multiplication function")

#function to divide two randomly generated numbers
def division():
    print("division")

#trialling random generator as part of v1 base component
def random_generator(num_1, num_2):
    rand_num = r.randint(num_1, num_2)
    return rand_num
#random generator component works well.



#set up lists and constants************************************
answer_list = []
yes_no_list = [["yes", "y"],["no","n"]]
operands = ["+","-","*", "/", "all"]


#set up main***************************************************
if __name__ == "__main__":
    #set local variables within the main routine
    min_num = 0
    max_num = 5

    print("placeholder")
    #ask users for input
    print("*******************MATH GAME****************************")
    print("**")
    print("** Welcome to my Math Game ")
    operand = input("** Choose an operand for your game - +, -, *, / or all: ")
    #check operand for legitimacy
    #string check - send the list of operands

    #ask user if they wish to use negatives?
    #yes/no list and answer sent to string checker

    #ask user for low and high numbers
    #int checker to check its an integer, loop until suitable integer

    #ask user for number of questions to be asked
    #int checker to check on the integer
    num_questions = 1

    #loop until number of questions is asked
    for questions in range(0, num_questions):
        #print("placeholder")
        if operand == "+":
            #print("go to addition")
            addition()
        elif operand == "-":
            #print("got to subtraction")
            subtraction()
        elif operand == "*":
            #print("go to multiplication")
            multiplication()
        elif operand == "/":
            #print("go to division")
            division()
        else:
            #this is called when user inputs all
            min_num = 1
            max_num = 5
            random_num = random_generator(min_num, max_num)
            print(random_num)
            #print("go to random generator, send min_num and max_num (1 and 5)")
            #print("then randomly go to each of the operand functions")
