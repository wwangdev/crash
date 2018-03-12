import printing_functions


# 8-1
def display_message():
    """
    We will learn function in this chapter
    """
    content = "function"
    print("we will learn " + content + " in this chapter")


display_message()


#8-2
def favorite_book(title):
    """

    """
    print("One of my favorite books is " + title.title())


book_name = "alice in wonderland"
favorite_book(title=book_name)


# 8-3
def make_shirt(size, mark="I love Python"):
    print("This shirt should have size of " + str(size) + " and with Mark: " + mark)


make_shirt(size=8, mark="SD")

# 8-4
make_shirt(size=12)
make_shirt(size=8)
make_shirt(size=2, mark="SD")


# 8-6
def city_country(city, country):
    return city.title() + ", " + country.title()


print(city_country("Santiago", 'chile'))
print(city_country('beijing', 'china'))
print(city_country('los angelas', 'america'))


# 8-7
def make_album(singer, album_title, number_songs=12):
    album = {
        'singer': singer,
        'album_title': album_title,
        'songs': number_songs
    }
    return album


print(make_album(singer='jay', album_title='lalala'))
print(make_album(singer='jay1', album_title='lalala2'))
print(make_album(singer='jay2', album_title='lalala3', number_songs=18))


# # 8-8
# while True:
#     print("Input info. q to quit")
#     singer = input("Name of singer: ")
#     if singer == 'q':
#         break
#     title = input("Name of album title: ")
#     if title == 'q':
#         break
#     songs = int(input("Number of songs: "))
#     if songs == 'q':
#         break
#     print(make_album(singer, title, songs))


# 8-9
def show_magicians(magician_list):
    for magician in magician_list:
        print(magician.title())


magician_list = ['aa', 'bb', 'cc']
show_magicians(magician_list)


# 8-10
def make_great(magician_list):
    for index in range(len(magician_list)):
        magician_list[index] = "the Great " + magician_list[index]
    return magician_list


make_great(magician_list)
show_magicians(magician_list)


# 8-11
magician_list_modified = make_great(magician_list[:])
show_magicians(magician_list)
show_magicians(magician_list_modified)


# 8-12
def sandwich_topping(*toppings):
    print("\nToppings: ")
    for topping in toppings:
        print("\t" + topping)


sandwich_topping('pep')
sandwich_topping("ll", 'bb', 'cc')
sandwich_topping('dd', 'ee')


# 8-13
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


print(build_profile('wal', 'ww', local='sd', age='33', city='dl'))


# 8-14
def make_car(made, module, **car_info):
    car = {}
    car['made'] = made
    car['module'] = module
    for key, value in car_info.items():
        car[key] = value
    return  car


print(make_car('honda', 'crv', color='silver', tow_package=True))


# 8-15
printing_functions.print_models('honda')

