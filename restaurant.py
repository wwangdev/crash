class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print("Name: " + self.restaurant_name)
        print("Type: " + self.cuisine_type)
        print("Number served: " + str(self.number_served))

    def open_restaurant(self):
        print(self.restaurant_name + " is now open")

    def increase_number_served(self, increased_num):
        if increased_num >= 0:
            self.number_served += increased_num
        else:
            print("Number of served should be >= 0")