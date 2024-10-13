
print("merchi")

c="sheliza"
print(c)

d=10.5
print(d)  #float value

e="saniyah"
print(e[3:])

print(c + '\t' + e)  # concatenation and escape character sequence applied 


A = 5
a= 10 
print(A)

A = B = C = 10 #equal variable values 
print(A)

#10/10/2024 

a = int(10)
a = 10 
a = float(10) 
a = str("Example")

a = "Taha"
b = "Sheliza"


print(a)
print(a + b) #cancatenate
print(a,b) #storing value as tuple 


myVar = 7 #camel case 
MyVarTest = 10 #All starting letters of words are capital 
my_var_test = 11

a = b = c = 1
print(b)

a , b , c = 2, 3 , 4 #assigning many variables to many values 
print(c)


d= 5 + 6j #complex numbers example 
print(d)
print(type(d))

f = 7.678
f_var = int(f)
print(f_var)


g = 10 
g_var = float(g)
print(g_var)

h_var = complex(f)
print(h_var)

g_var = complex(f)
print(g_var)




#11/10/2024

myVar=10
my_var=15
My_Var=20

myVar=int(10)

myVar=float(10)
print(myVar)

a= "test"
b= "example"

print(a+b)
print(a,b)

print(a + '\n' + b)

print(a + '\t' +  b)

a,b,c =1,2,3
print(b)


#list []
#tuple
#dictionary, {Key:Value}

"""
my_first_dict = {"Python": 5.5 , "Java": 7.5} #dictionary Values 
print(my_first_dict)
print(my_first_dict.keys())
print(my_first_dict.values())
print(my_first_dict["Java"])

"""

my_first_list= ["Banana", "Mango", "Orange"] #creating list 
x , y , z = my_first_list #unpacking items 
print(y)

d = "sheliza and taha have their \"Nikkah\"" #adding double quotes inside a string value 
e = "SHELIZA and taha \"Love\" each other"
print(len(d)) #printing number of letters in string 
print(d.capitalize())
print(d.upper())
print(e.lower())
print(e.startswith("sheliza"))
print(e.endswith("other"))
print(e.find("other"))
print(e.title())

print(d.splitlines())
print(d.strip())


#13/10/2024

e= "my love is \"taha\" merchant" 
print(e)
print(len(e))

print(e.upper())
print(e.title())
print(e.find("taha"))
print(e.capitalize())
print(e.startswith("n"))


my_dict= {"letter" : 7}
print(my_dict)
print(my_dict.keys())
print(my_dict.values())


print(10 > 9)
print(9 > 10)

high = 10 
low = 11 

print(high > low)
print(low > high)

if high > low :
    print("True")
else:
    print("False")

print(bool(2)) #using bool function to evaulate value 
print(bool("Taha"))
print(bool(3.5))
print(bool(""))
print(bool(0))

p = 5.6
print(isinstance(p, int)) #using isinstance method to get boolean value 


k = 3
k += 3
k -= 3
k /= 3
print(k)

print(z := 3)

my_list1 = ["Apple" , "Cherry" , "Mango"]
my_list2 = ["Apple" , "Cherry" , "Mango"]
my_list1 = my_list2
my_list2.append("Mango")
my_list2.append("Guava")
print(my_list2)
print(my_list1 is my_list2)

print("Cherry" in my_list1 )
print("cherry" not in my_list1)
print(my_list1 is not my_list2)

