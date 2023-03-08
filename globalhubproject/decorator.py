from pizza import Pizza

class Decorator(Pizza):

    def get_cost(self):
       return "\nIt costs "+ str(self.price)+" Turkish Liras."
    
    def get_description(self):
       return "Additional "+ self.description
 

class Olives(Decorator):
   def __init__(self):
        self.price = 7 
        self.description = "Olives"
    
class Mushrooms(Decorator):
    def __init__(self):
        self.price = 8
        self.description = "Mushrooms"

class Goat_Cheese(Decorator):
    def __init__(self):
        self.price = 10
        self.description = "Goat Cheese"

class Meat(Decorator):
    def __init__(self):
        self.price = 10
        self.description = "Meat"
    
class Onions(Decorator):
    def __init__(self):
        self.price = 5
        self.description = "Onions"
    
class Corn(Decorator):
    def __init__(self):
        self.price = 5
        self.description = "Corn"
   
