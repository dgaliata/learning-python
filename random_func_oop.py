basket = ["apple", "orange", "pear"]

basket.append("banana")

new_basket = basket

print (len(new_basket))

print (sorted(new_basket))

user = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "teams" : ["Sales", "Marketing", "Development"],
}

print(user["name"])
print(user["teams"][1])
print(user.items())

tuple_1 = (1, 8, 7)

print (tuple_1[1])

print (2 in tuple_1)

# ternary operator example
is_friend = False
can_message = "Message allowed" if is_friend else "Message not allowed"
print (can_message)

is_magician = True
is_expert = False

if is_magician and is_expert:
    print ("You are a master magician")
elif is_magician and not is_expert:
    print ("You are a magician")
else:
    print ("You are not a magician")


tf_block = {
    "cloud": "AWS",
    "region": "us-east-1",
    "instance_type": "t2.micro",
    "storage": "20 GB",
    "RAM": "2 GB",
    "Tags": "name_production_server"
}

print("Here are the details of your server:")

for value in tf_block.values():
    print(value)


test_list = [1, 2, 3, 4, 5]

counter = 0

for number in test_list:
    counter = counter + number
print (counter)


print (range(5))


mario_power_up = True

while mario_power_up is True:
    print ("Mario got a power up!")
    break
else:
    print ("Mario is small")


def company_name (name = "Aquia", location= "Remote"):
    print (f"Welcome to {name} your location will be {location}.")

company_name("Google", "Mountain View")
company_name()


name = "  John Doe  "


class EmployeeInfo:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: ${self.salary}")

emp1 = EmployeeInfo("Alice Smith", "Software Engineer", 90000)
emp2 = EmployeeInfo("Bob Johnson", "Data Scientist", 95000)

print(emp1.name)
