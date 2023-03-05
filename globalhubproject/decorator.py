from pizza import Pizza

class Decorator(Pizza):

    def get_cost(self):
       return self.component.get_cost() + Pizza.get_cost(self)
    
    def get_description(self):
       return self.component.get_description() + ' ' + Pizza.get_description(self)
    


class Olives(Decorator):
   def __init__(self, price, description):
        self.price = 7 
        self.description = description
    
class Mushrooms(Decorator):
    def __init__(self, price, description):
        self.price = 8
        self.description = description

class Goat_Cheese(Decorator):
    def __init__(self, price, description):
        self.price = 10
        self.description = description

class Meat(Decorator):
    def __init__(self, price, description):
        self.price = 10
        self.description = description
    
class Onions(Decorator):
    def __init__(self, price, description):
        self.price = 5
        self.description = description
    
class Corn(Decorator):
    def __init__(self, price, description):
        self.price = 5
        self.description = description
   
