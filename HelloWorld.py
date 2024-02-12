print("Hello world")
name = "John Smith"
age = 20
is_new = True

name = input("What is your name? ")
favourite_color = input("What is your favorite color? ")
print(name + " likes " + favourite_color)

birth_year = input("Birth year ")
print(type(birth_year))
age = 2024 - int(birth_year)
print(type(age))
print(age)

weight_lbs = input("Weight in pounds ")
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

course = "This is course"
course_copy = course[:]
print(course_copy)
first = "John"
last = "smith"
message = f'{first} [{last}] is a coder'
print(message)

course = "python for beginners"
print(len(course))
upper_course = course.upper()
print(upper_course)
print(course.replace("beginners", "absolute beginners"))

print("python" in course)
x = 10
x -= 3
print(x)
x = -2.9
print(abs(x))
import math
print(math.floor(2.9))
is_hot = False
is_cold = False
if is_hot:
    print("Its a hot day")
elif is_cold:
    print("its a cold day")

else:
    print("have a lovely day")

has_criminal_record = True
has_good_credit = False
if has_criminal_record and not has_good_credit:
    print("Eligible for a loan")
else:
    print("Not eligible for a loan")
name = input("Enter your name ")
if len(name) < 3:
    print("name must be at least three characters ")
elif len(name) > 50:
    print("name can be a maximum of 50 characters")
else:
    print("Name submitted successfully")
weight = input("Weight: ")
dimensions = input("(L)bs or (K)g: ")

if dimensions.upper() == "L":
    new_pounds = int(weight) * 0.45
    print(f"Your weight in kgs is {new_pounds}")
elif dimensions.upper() == "K":
    new_kgs = int(weight) / 0.45
    print(f"Your weight in pounds is {new_kgs}")
else:
    print("Please insert a correct value")
    quit()
i = 1
while i <= 5:
    print("*" * i)
    i = i + 1
print("Done")

number_of_guess = 1


while number_of_guess <= 3:
    number = 9
    guess = input("Guess a number: ")
    if int(guess) == number:
        print("You win")
        quit()
    else:
        print("You are close, guess again")
    number_of_guess += 1
print("You failed")

answer = input("> ").lower()
start = 0
stop = 0

while True:

    if answer == "help":
        print("""""
        Start - to start the car
        Stop - to stop the car
        quit - to exit
        """)
    if answer == "start" and start == 0:
        print("Car started...Ready to go")
        start += 1
    else:
        print("Car has already started")
    if answer == "stop" and stop == 0:
        print("The car stopped")
        stop += 1
    else:
        print("The car has already stopped")
    if answer == "quit":
        quit()
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
    print(total)
numbers = [5,2,5,2,8,2,10]
largest = numbers[1]
for x in numbers:
   if x > largest:
       largest = x
       print(largest)

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for row in matrix:
#     print(row)
#
# numbers = [5,5,5,3,2,2,1,7,4]
# unique_numbers = []
# numbers.insert(1,20)
# print(numbers)
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers)
# print(numbers2)
# for num in numbers:
#     if num not in unique_numbers:
#         unique_numbers.append(num)
# print(unique_numbers)
customer = {
     "name":"john smith",
     "age":30,
     "is_verified": True
 }
print(customer["name"])

phone = input("Phone: ")
digit_mapping = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
}
output = ""

for num in phone:
   output += digit_mapping.get(num, "!") + " "

print(output)

def greet_user(first_name, last_name):
    print(f"Hi there {first_name} {last_name}")
    print(f"Welcome aboard {first_name} {last_name}")



greet_user("John", "njoroge")
greet_user("mary", "wangui")

