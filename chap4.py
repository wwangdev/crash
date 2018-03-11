magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 4-1
pizzas = ['aa', 'bb', 'cc']
for pizza in pizzas:
    print("I love " + pizza.title())
print("I really love pizza!")

for value in range(1, 5):
    print(value)

for value in range(5):
    print(value)

numbers = list(range(1, 11, 2))
print(numbers)

squre = []
for value in range(1, 11):
    squre.append(value**2)
print(squre)
print(min(squre))
print(max(squre))
print(sum(squre))

squre = [value**2 for value in range(1,5)]
print(squre)

# 4-3
print([value for value in range(1,21)])

# 4-5
million = range(1, 1000001)
print(max(million))
print(min(million))
print(sum(million))

# 4-6
odd_numbers = range(1, 21, 2)
for num in odd_numbers:
    print(num)

# 4-9
cubic = [value**3 for value in range(1,11)]
print([num for num in cubic])

players = ['charles', 'martina', 'michael', 'florence','eli']
print(players[0:3])
print(players[:2])
print(players[1:])
print(players[-3:])

# NOTE: when copy the whole list, we need to use as list_des = list_src[:]!!!

# 4-13 tuple
foods = ('aa', 'bb', 'cc', 'dd', 'ee')
for food in foods:
    print(food)
foods = ('ff', 'gg')
for food in foods:
    print(food)