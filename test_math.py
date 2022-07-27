'''
requirements:
for 5-6 year olds
addition only
set up the main routine to run the program
set up a function for the addition
v1: set up the main routine
v2: check the loop works
v3: set up the addition function
v4: check the addition function is called
v5: create a random generator
'''
import random

# function for addition - takes 2 random numbers between 0 to 10,
# compares user answer with the calculated answer
def addition(num1, num2):
    # print("you are in the addition function")
    print("Answer is ", num1+num2)

    return

# this is an integer random number generator
# the function will receive two numbers, the minimum and the maximum range
# it will generate a random number between the min and the max
# it will return a random integer
def random_generator(min_num, max_num):
    ran_num = random.randint(min_num, max_num)
    print(ran_num)
    return ran_num

# main routine -------------------------------
# welcome statement

minimum_number_year1 = 0
maximum_number_year1 = 10
# loop through 10 times asking the question and calling the addition function
for question in range(0,10):
    # print(question)
    random_int_1 = random_generator(minimum_number_year1, maximum_number_year1)
    random_int_2 = random_generator(minimum_number_year1, maximum_number_year1)
    addition(random_int_1,random_int_2)


end_statement = "Thankyou for playing my game"
print(end_statement)
