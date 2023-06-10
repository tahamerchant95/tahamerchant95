# This project is about creating a simple calculator 

# need to ask user to enter two numbers

# add numbers
# subtract numbers
# divide numbers 
# multiple numbers 

# Need to take user input 
# when user is done with operation, ask user again if want to continue calculating 
# what if user enters negative numbers? what to do then?
# what if user enters wrong input 
# user might enter decimal values 
# with dividing numbers can throw an error of zero division
# have to provide user with choices as to what operation needs to carried out 
# user might enter a string value instead of integers or floats 


# first lets print out our choices to ask user 

# we can create functions for each operation

def add(num1, num2): # addition
    return num1 + num2

def sub(num1,num2): # subtraction
    return num1 - num2 

def multiply(num1,num2): # multiplication
    return num1 * num2

def divide(num1,num2): #division
    return num1 / num2 


# we have to ask user input now 
# we use a while loop so that user can continue doing calculations
# if have to stop calculation will break out of the loop
# what if user enters float and we at the moment have catsed input as float
# there can be decimal values, from which operations can be performed 
# hence we will need to cast input as float value 
# what if user enters wrong choice ?

while True:
    use_calc= input("Do you want to use calculator? (yes/no) ")
    if use_calc =="yes":
        print("Select choice:")
        print("1. Add:" + "+")
        print("2. Subtract:" + "-")
        print("3. Multiply:" + "*")
        print("4. Divide:" + "/")
        choices = float(input("Please enter choice:"))
    elif use_calc == "no":
        break
    else:
        print("Invalid input")

    try:
        if choices in (1, 2, 3, 4):
            num1= float(input("Enter first %s:"%("number")))
            num2= float(input("Enter second %s:"%("number")))
    except ValueError:
        print("Invalid %s entered please enter again:"%("number"))
        continue
    

    if choices == 1:
        print(num1, "+" , num2 , "=" , add(num1,num2))
    elif choices == 2 :
        print(num1, "-", num2, "=", sub(num1,num2))
    elif choices == 3 :
        print(num1, "*", num2, "=", multiply(num1,num2))
        
    elif choices == 4 : 
        try:
            print(num1, "/", num2 , "=", divide(num1,num2))
        except ZeroDivisionError: # we use exception so that error isnt thrown when divided by zero 
            print("Cannot divide by %s" %("zero"))
            continue


    
    
    

