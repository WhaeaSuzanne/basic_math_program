'''
26 May v1 component string checker - check to make sure the funciton is called. This is working.
26 May v2 ask user for input, check that it belongs inside a list of accepted answers. Loop until accepted answer is there,
return the accepted answer. Tested and works.
CC S.Anderson 2022
'''

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

# set up lists
yes_no_lst = [["yes","y"], ["no","n"]]
yes_no_err_msg = "Please enter yes or no."
negatives_ques = "Do you want to include negatives in your math questions? Enter either yes or no: "
# **main
#yes_no = str_checker(yes_no_lst, yes_no_err_msg, negatives_ques)

#loop input until the answer is returned as positive
valid = True
while valid == True:
    answer = input(negatives_ques)
    answer = answer.lower()
    answer = str_checker(yes_no_lst, yes_no_err_msg, answer)
    if answer == "yes" or answer == "no":
        valid = False
    else:
        print("This is not a valid answer. Please try again.")

print(answer)
