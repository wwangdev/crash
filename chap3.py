bicycles = ['trek', 'connondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[-2].upper())

# 3-1
names = ['JH', 'XXL', 'Zhai', 'Hui']
for index in range(names.__len__()):
    print(names[index].title())

# 3-2
for index in range(names.__len__()):
    print("Hello " + names[index])

# 3-3
transport = ['car', 'bicycle', 'motocycle']
print("I want to drive a " + transport[0])

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(2, 'lalala')
print(motorcycles)
del motorcycles[2]
print(motorcycles)
print(motorcycles.pop())
print(motorcycles)
print(motorcycles.pop(1))
print(motorcycles)
motorcycles.append('lalala')
motorcycles.append('lalala')
print(motorcycles)
motorcycles.remove('lalala')
print(motorcycles)

# 3-4
names = ['JH', 'XXL', 'Zhai', 'Hui']
for index in range(names.__len__()):
    print(names[index] + " is invited to dinner")

# 3-5
index = 1
print(names[index] + " cannot attend! ")
names[index] = 'FQ'
for index in range(names.__len__()):
    print(names[index] + ' is invitedto dinner')

# 3-6
print("Got a larger table. Invite three more!")
names.insert(0, 'AA')
names.insert(3, 'BB')
names.append('CC')
for index in range(names.__len__()):
    print(names[index] + ' is invitedto dinner')

# 3-7
print("Table is not available! Only two are invited")
while names.__len__() > 2:
    print("Sry, " + names.pop() + " is out!")
for index in range(names.__len__()):
    print(names[index] + ' is invitedto dinner')
while names.__len__():
    del names[0]
print(names)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars, reverse=True))
cars.reverse()
print(cars)
print(len(cars))

# 3-8
place_togo = ['Hawaii', 'Japan', 'Tailand', 'Yellowstone', 'Alaska']
print(place_togo)
print(sorted(place_togo))
print(place_togo)
print(sorted(place_togo, reverse=True))
print(place_togo)
place_togo.reverse()
print(place_togo)
place_togo.reverse()
print(place_togo)
place_togo.sort()
print(place_togo)
place_togo.sort(reverse=True)
print(place_togo)
