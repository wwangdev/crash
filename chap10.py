import json
# # 10-1
# file_name = 'learning_python.txt'
# with open(file_name, 'w') as content:
#     prefix = 'In Python you can '
#     content.write(prefix + "use lots of APIs\n")
#     content.write(prefix + "quickly do simulation\n")
#
# with open(file_name) as content:
#     text = content.read()
#     print(text)
#
# with open(file_name) as content:
#     for line in content:
#         print(line.rstrip())
#
# with open(file_name) as content:
#     lines = content.readlines()
#
# for line in lines:
#     print(line.rstrip())
#
#
# # 10-2
# replaced_text = text.replace('Python', 'C')
# print("\n" + replaced_text)
#
# for line in lines:
#     print(line.replace('Python', 'C++').rstrip())
#
#
# # 10-4
# file_name = 'guest.txt'
# while True:
#     guest_name = input("Enter the guest name('q' to exit): ")
#     if guest_name == 'q':
#         break
#     with open(file_name, 'a') as guest:
#         guest.write(guest_name + "\n")
#
#

# # 10-6 & 10-7
# while True:
#     num_1 = input("First Number: ")
#     if num_1 == 'q':
#         break
#     num_2 = input("Second Number: ")
#     if num_2 == 'q':
#         break
#     try:
#         num_1 = int(num_1)
#         num_2 = int(num_2)
#         print("Sum: " + str(num_2 + num_1))
#     except ValueError:
#         print("Please make sure the inputs are both numbers")


# 10-10
file_name = 'catty.txt'
try:
    with open(file_name) as content:
        text = content.read()
        words = text.split()
        print("Number of words " + str(len(words)))
        print("Number of 'I's " + str(words.count('I')))
        print("Number of 'he's " + str(text.lower().count('he')))
except FileNotFoundError:
    print("No such file: " + file_name)


# 10-11
file_name = 'favorite_number.json'
# number = input("Your favorite number is: ")
# with open(file_name, 'w') as f_obj:
#     json.dump(number, f_obj)

with open(file_name) as f_obj:
    number_r = json.load(f_obj)
print(number_r)



