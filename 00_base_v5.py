'''
game to ask basic math questions
base component
v1 - set up the skeleton of the program, test the functions are called as required
v2 - trial random generator function component. Works well so will keep it
V3 - add int checker function component to the base component - tested and running, trialled the questions for low and high num
v4 - add string checker function to base component. Works for yes_no.
v4.1 -  add string check for checking operand works
v5 - add the addition function to the base component
CC SA 2022

'''
#import library************************************************
import random as r

#set up functions**********************************************

#function to check for integers. will loop until an integer is input
#checked this and is working @25/5/22
def int_checker(question, error_message):
    x = True
    while x == True:

        try:
            int_num = int(input(question))
            x = False
        except:
            print(error_message)

    return(int_num)


#function to check string is within an allowable list. Will loop until an allowable word is input
#str checker function - checks a string input is within a list of acceptable answers, returns the answer.
def str_checker(gen_lst, err_msg, choice):
    is_valid = ""
    chosen = ""

    for option in gen_lst:
        if choice in option:
            chosen = option[0]
            break
        else:
            chosen = "not_valid"

    return chosen


#function to ADD two randomly generated numbers
def addition(min_num, max_num):
    #print ("addition") testing
    #random generate two numbers
    num1 = random_generator(min_num,max_num)
    num2 = random_generator(min_num,max_num)
    answer = int(input(str(num1) + " + " + str(num2) +  " = "))
    if answer == (num1 + num2):
        print("that is the correct answer. Well Done! :)")
        answer = "correct"
    else:
        print("Sorry, that is not the answer. The correct answer is ", num1 + num2)
        answer = "incorrect"
    return answer

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
yes_no_lst = [["yes", "y"],["no","n"]]
operands = ["+","-","*", "/", "all"]


#set up main***************************************************
if __name__ == "__main__":
    #set local variables within the main routine
    #*******CHANGE the hard coded numbers **********
    min_num = 0 #set up the minimum number variable - int
    max_num = 0 #set up the maximum number variable - int
    num_of_questions = 0 #set up the num of questions variable - int
    score = 0 #set up the score variable - int
    num_correct = 0
    #set up any lists
    hi_score_lst = []

    #set up text strings variables
    err_msg = "Not a valid answer."
    quest_str = "" #variable ready to be populated depending on the question
    #ask users for input

    print("*******************MATH GAME****************************")
    print("**")
    print("** Welcome to my Math Game ")

    #check operand for legitimacy
    #string check - send the list of operands
    valid = True #valid must re-initialised every time it is run in a loop
    operand_lst = ["+", "-", "*", "/", "all"]
    ques_str = "** Choose an operand for your game - +, -, *, / or all: "
    operand_err = "Not a valid answer."

    while valid == True:
        operand = input(ques_str)
        operand = operand.lower()
        operand = str_checker(operand_lst, operand_err, operand)

        if operand == "not_valid":
            print("This is not a valid answer. Please try again.")
        else:
            valid = False

    # print("Testing operands ", operand) *******

    #ask user if they wish to use negatives?
    #yes/no list and answer sent to string checker
    #loop input until the answer is returned as positive
    #move to yes_no area

    ques_str = "Do you want to include negatives in your math questions? Enter either yes or no: "
    valid = True #valid must re-initialised every time it is run in a loop

    while valid == True:
        answer = input(ques_str)
        answer = answer.lower()
        answer = str_checker(yes_no_lst, err_msg, answer)
        if answer == "not_valid":

            print("This is not a valid answer. Please try again.")
        else:
            valid = False

    #print("Testing negatives ", answer)

    #ask user for low and high numbers
    #int checker to check its an integer, loop until suitable integer
    min_num = int_checker("Please enter a low number: ", "This is not an integer - please enter an integer: ")

    max_num = int_checker("Please enter a high number: ", "This is not an integer - please enter an integer: ")


    #ask user for number of questions to be asked using int_checker function
    num_questions_quest = "how many questions do you want to answer? "
    num_questions = int_checker(num_questions_quest, err_msg)

    #loop until number of questions is asked
    for questions in range(num_questions):
        #print("placeholder")
        if operand == "+": #call the addition function the number of times asked for
            #print("go to addition")
            num_correct = addition(min_num, max_num)
            hi_score_lst.append(num_correct)
            print(hi_score_lst)
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

    #print out the correct score count
    #count through the list and add the score of correct answers
    for num_correct in hi_score_lst:
        if num_correct == "correct":
            score += 1

    print("you have answered " , score , "of ", num_questions, "correctly.")

    #end score
