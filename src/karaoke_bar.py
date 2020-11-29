from src.guest import Guest
from src.drink import Drink

class Karaoke_Bar():

    def __init__ (self):
        self.register = {}
        self.drinks = []
        self.guests = []
        self.till = 0


    def sell_drink_to_guest (self, drink, guest):
        if drink.price <= guest.money:
            guest.money -= drink.price
            self.till += drink.price
            self.guests.append (guest.name)

        if guest in self.guests:
            self.register[guest.name]["Purchase History"].append(drink.name)
            self.register[guest.name]["Money transactions"].append(drink.price)

        else:
            self.register [guest.name] = {
                "Purchase History" : [],
                "Money transactions" : []
                }
            self.register[guest.name]["Purchase History"].append(drink.name)
            self.register[guest.name]["Money transactions"].append(drink.price)

    # if a guest is in the bar guests lists already, update their dictionary items, if not, create new dictionary
    # for guest and update accordingly.
    # If a guest has multiple transactions however, the 2 lists are not updated. Their values are instead replaced,
    # keeping only one Drink and one money transaction recorded.

    







# REGISTER STRUCTURE EXAMPLE #

# self.register = {
#     "Angelo" : {
#         "Purchase History" : [drink_1.name, drink_2.name]
#         "Money spent" : [drink_1.price, drink_2.price]
#     }
#     "Ryan" : {
#         "Purchase History" : [drink_1.name]
#         "Money spent" : [drink_1.price]
#     }
                
# }