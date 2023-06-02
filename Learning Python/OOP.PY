lst = [2,2,3,4,5]

print(lst.count(2))

print(type(1)) #   object is int type
print(type(())) # object is tuple type 
print(type({})) # object is dictionary 
print(type([])) # object is list


# classes allow us to define objects on our own 
# using the class keyword
# need to define instance in class 
# need to instantiate class
# need to create attributes within our class 
# to create attributes need to use self keyword 
# attribute is a characteristic of an object 
# method is an operation that needs to be performed on an object 

class Example():
    pass
x= Example()

print(type(x))


class Cat():
    def __init__(self, breed): 
        self.breed= breed

sasha = Cat(breed='persian')

sasha.breed # no paranthesis after breed since its an attribute so it doesnt take any attributes


class Cat():

    species= "Mammals" #class object attribute and defined outside any methods in class

    def __init__(self, breed, name):
        self.breed= breed
        self.name = name

kiara= Cat('Persian', 'kiara')

print(kiara.name)
print(kiara.breed)
print(kiara.species)

class Circle():
    pi= 3.14

    def __init__(self, radius=1):
        self.radius= radius
        self.area= radius * radius * Circle.pi # class object attribute

    def setRadius(self, new_radius):
        self.radius= new_radius
        self.area= new_radius * new_radius * self.pi

    def getCircumference(self):
        return self.radius * self.pi * 2
    
c= Circle()
c.setRadius(3)

print('Raidus is: ' , c.radius)
print('Area is: ', c.area)
print('Circumference is: ' , c.getCircumference())


# inheritance allows to create new classes using existing classes
# newly formed classes are called derived classes
# the classes that we derive from are called base classes
# inheritance allows code reuse 
# derived classes allow to extend functionality or override class


class Animal(): #base class
    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("Animal")
    
    def eat(self):
        print("Eating")

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cat created")

    def whoAmI(self):
        print("Cat")
    
    def bark(self):
        print("meow")

d= Cat()
d.whoAmI()
d.bark()
d.eat()


# polymorphism is a way in which different object classes share same method name'
# can use abstract class and inheritance 
# abstract class never expects to be instantiated

class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("subclass must implement abstract method")
    
class Dog(Animal):
    def speak(self):
        return self.name + " Says woof "


class Cat(Animal):
    def speak(self):
        return self.name +" Says Meow "
    

zippy=Dog("Zippy")
sasha= Cat("Sasha")

print(zippy.speak())
print(sasha.speak())


# polymorphism can be presented as a function

for pets in [zippy,sasha]:
    print(pets.speak())

def pet_speak(pets):
    print(pets.speak())

pet_speak(zippy)
pet_speak(sasha)


class Book():
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title= title
        self.author= author
        self.pages= pages 
 
    def __str__(self):
        return "Title: %s, author %s, pages:%s "%(self.title,self.author,self.pages)
    
    def __len__(self): # special method to get lenght
        return self.pages
    
    def __del__(self): # special method to remove item 
        print("A book is removed")

book= Book("Python for begginners ", "Merchant", 170)

print(book)
print(len(book))
del book 


