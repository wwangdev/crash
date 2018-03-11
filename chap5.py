# 5-2
str_1 = 'audi'
str_2 = 'bmw'
print(str_1 == str_2)
print(str_1 != str_2)
num_1 = 15
num_2 = 22
print(num_1 > num_2)
print(num_1 == num_2)
print(num_1 < num_2)
print(num_1 != num_2)
print(str_1 != str_2 and num_1 < num_2)
print(str_1 < str_2 or num_1 == num_2)
cars = ['bmw', 'audi', 'honda']
print('audi' in cars)
print('toyota' in cars)

# 5-3
alien_color = 'green'
if alien_color == 'green':
    print("Player got 5 points")
else:
    print("No point added")

# 5-5
point = 0
if alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
elif alien_color == 'red':
    point = 15
else:
    point = 0
print("player got " + str(point) + " points!")

# 5-8 & 5-9
names = ['admin', 'mike', 'david', 'roy', 'jay']
# names = []
if names:
    for name in names:
        if name == 'admin':
            print("Hello admin, status report?")
        else:
            print("Hello " + name.title() + ", thanks for login")
else:
    print("We need to find some users!")

# 5-10
current_users = ['admin', 'Mike', 'david', 'roy', 'jay']
current_users = [user.lower() for user in current_users]
print(current_users)
new_users = ['tim', 'Mike', 'alice', 'jay']
for user in new_users:
    if user.lower() in current_users:
        print("User exist, other names")
    else:
        print(user + " is not used")

# 5-11
numbers = range(1, 10)
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    else:
        print(str(number) + "th")

