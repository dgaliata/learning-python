# x = 3.2
# y = 4.6
# z = round(x+y)
# print(z)

# x = float(input("give me a number"))
# y = float(input("give me another number"))

# z = round = (x + y)

# print(f"{z:,}")

# def hello():
# name = input("What is your name? ")
# print(f"Hello {name}")

# hello()

# > greater than
# >= greater than or equal to
# < less than
# <= less than or equal to
# == equality
# != not equal to

i = 0
while i < 3:
    print("Python")
    i = i + 1

for _ in range(3):
    print("Cool")

print("Hi\n" * 3, end="")

while True:
    n = int(input("Guess the lucky number! "))
    if n > 3:
        print("try again")
    elif n <= 3:
        print(f"You got it! {n} is the lucky number! ")
        break

names = ["Harry", "Ron", "John"]
names.append("Hermione")
print(names)

for i in range(len(names)):
    print(names[i])

student_numbers = [1,2,3,4,5]
user_input = input("Guess how many students we have ")
for student_numbers in user_input:
    print("Nice Guess! We have 5 students")

set = {1, "Test", 77}
print(set)

mario_bros = {"Mario": ["Red Plummer", "Small", "Main Character"], "Luigi": ["Green Plummer", "Funny", "Jumps Higher"]}
print(mario_bros["Luigi"][1])

numbers = range(4)
for number in numbers:
    print(f"{numbers}: This is a short list")

pb_cookie = ["Peanut Butter", "Eggs", "Sugar"]
for i, ingredient in enumerate(pb_cookie):
    print(i, ingredient)

def create_user_mapping(username, department, title):
   print(f"Thank you. The new employee has the following username {username} and has been assigned to the {department} department. Their title is {title}.")

create_user_mapping("John Doe", "IT", "Systems Administrator")

characters = ["Mario", "Link", "Donkey Kong",]
for character in characters:
    print(f"{character.title()} you're a Nintendo video game character")

copy_characters = characters[:]
print(copy_characters)

print("There are no XBOX characters in the list")

first_numbers = list(range(1,11))
print(first_numbers)


drinking_age = int(input("How old are you? ")) #Use int(input()) when you need a number for calculations or comparisons

if drinking_age >= 21:
    print ("You are old enough to drink")

else:
    print ("Not old enough!")
    
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
# Prompt for the person's name and response.

    name = input("\nWhat is your name? ")

response = input("Which mountain would you like to climb someday? ")

# Store the response in the dictionary.
responses[name] = response

# Find out if anyone else is going to take the poll.

repeat = input("Would you like to let another person respond? (yes/ no) ")
if repeat == 'no':
    polling_active = False

# Polling is complete. Show the results.
# 
# print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")