'''
addition function
v1 first version of the addition function.
I want it to:
get a random number between the min and max numbers
print them out on an input for the user to answer
check the answer is correct or not
print out
if correct, then Well Done
if not, then print the correct answer
v2 make the function run for multiple questions



CC SA 2022
'''
import random as r

def random_generator(num_1, num_2):
    rand_num = r.randint(num_1, num_2)
    return rand_num

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


#**************MAIN ROUTINE*****************
#testing the program with hard coded numbers
min_num = 0
max_num = 100
num_of_questions = 10
hi_score_lst = []
#call addition function, multiple times
for question_num in range(num_of_questions):
    answer_hi_score = addition(min_num, max_num)
    hi_score_lst.append(answer_hi_score)

print(hi_score_lst)
