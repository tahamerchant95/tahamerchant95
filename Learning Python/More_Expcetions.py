try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print("Printed Values")


x = 5
y = 0 

try:
    z = x / y
    print(z)

except ZeroDivisionError:
    print("Value cant be divided")

finally:
    print("done with program")


def ask():
    while True:
        try:

            user= int(input("Please enter value to square it: "))
        except:
            print("An error occured: ")
            continue
        else:
            break

    print("your number squared is: ", user**2 )

ask()