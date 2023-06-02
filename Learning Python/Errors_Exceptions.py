#errors and exceptions may occur while writing code

# for instance Syntax errors will give an end of line error

# will use try and except statement to handle exceptions 

# try keyword will be used to put code inside it that can cause errors

# except keyword wwill be used to implement the exception

# finally keyword will allow to run the code even if exception is raised



try:
    f = open("examplefile", 'w')
    f.write("testing.... ")
except IOError: # will only check for IOError exception and execute print statament 
    print("Error: could not find file or read data")

else:
    print("text added")
    f.close()

def enter_int():
    while True:

        try:
            user= int(input("enter integer please: "))
    
        except:
            print("You didnt enter integer: ")
            continue

        else:
            print("entered correct integer ")
            print(user)
            break

    
        finally:
            print("Finally entered: ")
            
enter_int()
