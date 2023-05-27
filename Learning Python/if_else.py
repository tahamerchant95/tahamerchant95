# if-else allows to specify multiple conditions
# if condition1 happens then do something
# else if condition 2 happens do something
# else do nothing 
# indentation is really important when it comes to check conditions and executing loops



if True:
    print('statement is true ')


fruit= 'Apple' #assinging a variable with value Apple

if fruit == 'Orange': #if condition one false move to next condition
    print('color of orange is orange')
elif fruit =='Apple': #if condition two true execute this statement
    print("color of Apple is red")
else:
    print("No fruits are available to buy") #final condition

