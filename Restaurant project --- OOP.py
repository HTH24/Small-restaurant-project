# -*- coding: utf-8 -*-
"""
Created on Sun May 17 09:55:01 2020

@author: 胡天行
"""


from datetime import time

# Create a menu
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return self.name + " is served from " + str(self.start_time) + " to " + str(self.end_time)

  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      total += self.items[item]
    return total

brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu('brunch', brunch_items, time(hour = 11), time(hour = 16))
# served from 11am to 4pm

early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu('early bird', early_bird_items, time(hour = 17), time(hour = 23))
# served from 5pm to 11pm ---> 17 and 23
dinner_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
# served from 5pm to 11pm
dinner = Menu('dinner', dinner_items, time(hour = 17), time(hour = 23))

kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
# served from 11am until 9pm. 11 and 21
kid = Menu('kid', kids_items, time(hour = 11), time(hour = 21))

print(brunch)
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# Create another restaurant with another menu
class Franchise:
  def __init__(self, address, menu):
    # address is a string, menu is a list of Menus
    self.address = address
    self.menus = menu

  def __repr__(self):
    return "Address of the restaurant is " + self.address
  
  def available_menus(self, time):
    l = []
    for menu in self.menus:
      if (time >= menu.start_time) & (time <= menu.end_time):
        l.append(menu)
    return l


menu_list = [brunch, early_bird, dinner, kid]

flagship_store = Franchise('1232 West End Road', menu_list)
new_installment = Franchise('12 East Mulberry Street', menu_list)

print(flagship_store)
# Notice that here the parameter of available_menus method needs to be a time object.
print(flagship_store.available_menus(time(hour = 12)))
print(flagship_store.available_menus(time(hour = 17)))

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchise = franchises
  def __repr__(self):
    return "Our new business: " + self.name

franchise_list = [flagship_store, new_installment]

first_business = Business('Basta Fazoolin\' with my Heart', franchise_list)
print(first_business)

arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_menu = Menu('arepas', arepas_items, time(hour = 10), time(hour = 20))
print(arepas_menu)

menu_list_updated = menu_list.append(arepas_menu) 

arepas_place = Franchise('189 Fitzgerald Avenue', menu_list_updated)

print(arepas_place)



    