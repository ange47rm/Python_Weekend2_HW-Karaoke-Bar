from src.guest import Guest
from src.drink import Drink

class Karaoke_Bar():

    def __init__ (self):
        self.register = {}
        self.drinks = []
        self.guests = []

    def sell_drink_to_guest (self, drink, guest):
        if drink.price <= guest.money:
            guest.money -= drink.price
            self.guests.append (guest.name)



        # if guest not in
        #     self.register [guest.name] = {
        #         "Purchase History" : []
        #         "Money transactions" : []
        #         }


        #     self.register[guest.name]["Purchase History"].append(drink.name)
        #     self.register[guest.name]["Money transactions"].append(drink.price)



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