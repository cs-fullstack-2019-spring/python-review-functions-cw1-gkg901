def main():

    # ex1()
    ex2()


def dothemath(n1,n2):
    myDict = {"SUM": n1+n2,"DIFF":n1-n2,"PROD":n1*n2,"QUOT":n1/n2}
    return myDict






# Create a function that has a loop
# Prompt for numbers until the user enters q to quit
# If the user doesn't enter q, ask them to input another number
# When the user enters q to quit, print the SUM of all numbers entered
def ex1():


    nums = []
    userInput = ""
    while (userInput != 0):
        userInput = int((input("enter a number")))
        nums.append(userInput)

        print(sum(nums))






# Create a function problem2()
# In this function prompt the user for 2 numbers
# Create a second function called do_the_math that accepts 2 parameters (the 2 entered numbers)
# In the do_the_math calculate the SUM, DIFFERENCE, PRODUCT, and QUOTIENT (division result)
# and return them as a dictionary to the calling function
# Example: Dictionary result returned if the arguments 25 and 10 are passed to the function:
# {'diff': 15, 'prod': 250, 'quot': 2.5, 'sum': 35}
# In your problem2() function, print the dictionary result
# returned from your do_the_math function using string literal formatting

def ex2():

    num1 = int(input("enter a number\n"))
    num2 = int(input("enter a number\n"))

    result = dothemath(num1,num2)
    print(f'Here are your results for the numbers {num1} and {num2}')
    print(f'The SUM result is {result["SUM"]}')
    print(f'The DIFFERENCE result is {result["DIFF"]}')
    print(f'The PRODUCT result is {result["PROD"]}')
    print(f'The DIVISION result is {result["QUOT"]}')

























if __name__ == '__main__':
    main()