class Pizza:
    def __init__(self, price, description):
        self.price = price
        self.description = description

    def get_description(self):
        return "It's a " + self.description

    def get_cost(self):
        return "It costs " + self.price + "Turkish Liras"


class Classic(Pizza):
    def __init__(self):
        self.name = "Classic"
        self.price = 40
        self.description = "crusted pizza, grated mozzarella, rich tomato sauce with the sauces you want."

class Margherita(Pizza):
    def __init__(self):
        self.name = "Margherita"
        self.price = 30
        self.description = "typical Neapolitan pizza, made with San Marzano tomatoes, mozzarella cheese, fresh basil, salt, and extra-virgin olive oil."
    
class Turk_Pizza(Pizza):
    def __init__(self):
        self.name = "Turk Pizza"
        self.price = 25
        self.description = "Lahmacun - categorically thin, crispy pizza toppings of flavor crammed mixture of milled meat with peppers, fresh herbs, earthy spices and tomato."
    
class Dominos_Pizza(Pizza):
    def __init__(self):
        self.name = "Dominos Pizza"
        self.price = 60
        self.description = "pizza with special dominos sauce."
