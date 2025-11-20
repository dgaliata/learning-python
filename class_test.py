class character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

class Hero(character):
    def __init__(self, name, health, attack, super_power):
        super().__init__(name, health, attack)
        self.super_power = super_power

hero = Hero("Superman", 100, 50, "Flight")

print (f"Hero Name: {hero.name}")

print(hero.attack)
    

class user_details:
    def __init__(self, name, age, city, teams):
        self.name = name
        self.age = age
        self.city = city
        self.teams = teams
   
user1= user_details("Alice", 30, "New York", ["TeamA", "TeamB"])
user2= user_details("Bob", 25, "Los Angeles", ["TeamC", "TeamD"])
user3= user_details("Charlie", 28, "Chicago", ["TeamE", "TeamF"])

def display_user_info(user1):
    print(f"Name: {user1.name}")
    print(f"Age: {user1.age}")
    print(f"City: {user1.city}")
    print(f"Teams: {', '.join(user1.teams)}")

display_user_info(user3)