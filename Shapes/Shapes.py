from math import pi 

class Circle(): # creating a Circle class object 
    def __init__(self, radius):
        self.radius = radius
        

    def area(self):
        return pi * self.radius * self.radius
    
    def perimeter(self):
        return 2 * pi * self.radius

class Rectangle(): #creating reactangle object 
    def __init__(self, height, width):
        self.height= height
        self.width= width 

    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return (self.width + self.height) * 2 

class Triangle(): # creating traingle object
    def __init__(self,side_a,side_b, side_c):
        self.side_a= side_a
        self.side_b= side_b
        self.side_c = side_c

    def area(self): # calculating area of triangle
        a= (self.side_a + self.side_b + self.side_c) / 2 

        area= (a * (a - self.side_a) * (a - self.side_b) * (a - self.side_c))

        return area 

    def perimeter(self): # calculating perimeter of triangle 
        return self.side_a + self.side_b + self.side_c
    


class Sphere(): #creating sphere object 
    def __init__(self, radius):
        self.radius= radius 

    def surface_area(self):
        return 4 * pi * self.radius**2
    
    def volume(self):
        return ((4/3) * (pi * self.radius**3))



