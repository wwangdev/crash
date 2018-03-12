# 6-1
xxl= {}
xxl['first_name'] = 'Xin'
xxl['last_name'] = 'Liu'
xxl['age'] = 32
xxl['city'] = 'Kaifeng'
print(xxl)

# 6-3
dict = {}
dict['int'] = 'Integer'
dict['float'] = 'Floating point'
dict['none'] = 'None'
dict['dictionary'] = 'Dictionary type'
dict['list'] = 'List type'

for key,value in dict.items():
    print("Key: " + key)
    print("Value: " + value + "\n")

# 6-5
rivers = {}
rivers['nile'] = 'egypt'
rivers['Yangzi'] = 'china'
rivers['Amazon'] = 'colombia'

for key,value in rivers.items():
    print("The " + key.title() + ' runs through ' + value.title())

print("\nRivers: ")
for key in rivers.keys():
    print(key.title())

print("\nCountries: ")
for value in rivers.values():
    print(value.title())

# 6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
investigated_list = ['sarah', 'ww', 'phil', 'jh']
for name in investigated_list:
    if name in favorite_languages.keys():
        print("Thanks " + name.title() + " for taking the investigation")
    else:
        print("Hi " + name.title() + ", please take the investigation")

# 6-7
wal = {
    'first_name': 'wal',
    'last_name': 'wang',
    'age': 34,
    'city': 'dalian'
}
jh = {
    'first_name': 'jj',
    'last_name': 'he',
    'age': 35,
    'city': 'beijing'
}
people = [xxl, wal,jh]
for person in people:
    print("\nFirst name: " + person['first_name'].title())
    print('Last Name: ' + person['last_name'].title())
    print('Age: ' + str(person['age']))
    print('City: ' + person['city'].title())

# 6-9
favorite_places = {}
favorite_places['xxl'] = ['sd', 'sh', 'gz']
favorite_places['wal'] = ['dl', 'sd']
favorite_places['jh'] = ['sj', 'bj', 'cd']
for key, values in favorite_places.items():
    print(key + " loves: ")
    for place in values:
        print('\t' + place)





