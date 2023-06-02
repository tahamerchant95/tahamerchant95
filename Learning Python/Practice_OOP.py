# writing function to return slop and distance of line 
# using oop to write 

class Line_dis(object):

    def __init__(self, cor1, cor2):
        self.cor1= cor1
        self.cor2= cor2

    def get_distance(self):
        x1,y1= self.cor1
        x2, y2= self.cor2

        return ((x2-x1)**2 + (y2-y1)**2) ** 0.5
    
    def get_slope(self):
        x1,y1= self.cor1
        x2,y2= self.cor2
        return (y2-y1)/(x2-x1)
    
coordinate1= (2,5)
coordinate2= (3,6)

li= Line_dis(coordinate1,coordinate2)

print(li.get_distance())
print(li.get_slope())


#############################################################


# calculate volume of cylinder 
# calculate surface area of cylinder

class Cylinder:
    def __init__(self, radius=1, height=1):
        self.height= height
        self.radius= radius
    
    def volume(self):
        return self.height * 3.14 * (self.radius) ** 2 
    
    def surface_area(self):
        top = 3.14 * (self.radius) ** 2
        return (2*top) + (2 * 3.14 *self.radius * self.height)
    
cy= Cylinder(3,4)
print(cy.volume())
print(cy.surface_area())

################################################

#create bank account function
# deposit cash
# withdraw cash 

class Account:
    def __init__(self, deposit, balance = 0 ):
        self.deposit= deposit
        self.balance= balance
        

    def Deposit_Account(self,deposit):
        self.balance= self.balance + self.deposit
        return deposit
    
    def withdraw_Account(self, withdraw):
        if self.balance >= withdraw:
            self.balance= self.balance - withdraw
            print("Withdraw %s" %("Accepted"))
        
        else:
            print("Funds %s" %("unavailable"))
    
a= Account(100)
print(a.Deposit_Account(100))
print(a.Deposit_Account(200))
print(a.withdraw_Account(300))
print(a.withdraw_Account(100))





