# # 7-1
# car = input("What kind of car are you looking for? ")
# print("Let me see if I can find you a " + car.title())
#
# # 7-2
# people = input("How many people for reservation: ")
# if int(people) > 8:
#     print("Not available")
# else:
#     print("Table ready")
#
# # 7-3
# number = input("Please enter the number: ")
# if int(number) % 10 == 0:
#     print("The number is multiple of 10")
# else:
#     print("The number is not multiple of 10")

# # 7-4
# while True:
#     topping = input("What topping do you want? Type 'q' to exit: ")
#     if topping == 'q':
#         print("User finished order")
#         break
#     print("We will add " + topping)

# 7-8
sandwich_orders = ['pas', 'tuna', 'pas', 'steak', 'vege', 'pas']
finished_sandwich = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwich.append(sandwich)
    print(sandwich + " made!")
print("finished sandwich: ")
for sandwich in finished_sandwich:
    print(sandwich)

# 7-9
sandwich_orders = ['pas', 'tuna', 'pas', 'steak', 'vege', 'pas']
print("Pas is sold out")
while 'pas' in sandwich_orders:
    sandwich_orders.remove('pas')
for sandwich in sandwich_orders:
    print(sandwich)

