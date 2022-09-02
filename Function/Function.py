
# Addition function
def add_num(num1,num2):
    return num1+num2
add_num(4,5)
# Can also save as variable due to return
result = add_num(4,5)
print(result)

#Check if any number in a list is even

def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop
    return False

    check_even_list([1, 2, 3])