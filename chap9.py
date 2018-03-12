import restaurant as rt
from collections import OrderedDict
from random import randint
# # 9-1 & 9-4
# class Restaurant:
#     def __init__(self, name, type):
#         self.restaurant_name = name
#         self.cuisine_type = type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print("Name: " + self.restaurant_name)
#         print("Type: " + self.cuisine_type)
#         print("Number served: " + str(self.number_served))
#
#     def open_restaurant(self):
#         print(self.restaurant_name + " is now open")
#
#     def increase_number_served(self, increased_num):
#         if increased_num >= 0:
#             self.number_served += increased_num
#         else:
#             print("Number of served should be >= 0")
#
#
# rest = Restaurant("tea station", "Taiwan")
# rest.describe_restaurant()
# rest.open_restaurant()
# rest.number_served = 3
# rest.describe_restaurant()
# rest.increase_number_served(100)
# rest.describe_restaurant()
# rest.increase_number_served(-20)
# rest.describe_restaurant()
#
#
# class IceCreamStand(Restaurant):
#     def __init__(self, name, type):
#         super().__init__(name, type)
#         self.flavors=[]
#
#     def describe_ice_cream_stand(self):
#         super().describe_restaurant()
#         print("Flavors: ")
#         for flavor in self.flavors:
#             print("\t" + flavor)
#
#     def add_flavor(self, flavors):
#         for flavor in flavors:
#             self.flavors.append(flavor)
#
#
# ice_cream_stand = IceCreamStand("tea", "Taiwan")
# flavors = ['mint', 'cho', 'strawberry']
# ice_cream_stand.add_flavor(flavors)
# ice_cream_stand.describe_ice_cream_stand()


# 9-10
restaurant = rt.Restaurant("tea", "Taiwan")
restaurant.describe_restaurant()


# 9-11
dict = OrderedDict()
dict['int'] = 'Integer'
dict['float'] = 'Floating point'
dict['none'] = 'None'
dict['dictionary'] = 'Dictionary type'
dict['list'] = 'List type'

for key, value in dict.items():
    print("Key: " + key + "\tvalue: "+value)


# 9-12
class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        return randint(1, self.sides)


die_6 = Die()
die_6.sides = 6
die_20 = Die()
die_20.sides = 20
print("6 Sides: ")
for index in range(10):
    print(die_6.roll_die())

print("20 Sides: ")
for index in range(10):
    print(die_20.roll_die())