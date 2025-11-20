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
    