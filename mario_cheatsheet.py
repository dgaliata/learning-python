# Mario Python Cheatsheet

# Data Types

# Numbers
coins = 42            # integer
jump_height = 3.14    # float
star_power = 1 + 2j   # complex number

# Strings
character = "Mario"   # can use single or double quotes
mario_quote = """
It's-a me,
Mario!
"""

# Booleans
has_mushroom = True
is_small = False

# None type
empty_block = None    # represents absence of value

# Variables

# Basic assignment
lives = 3
player_name = "Luigi"

# Multiple assignment
coins, stars, mushrooms = 100, 5, 2

# Variable naming rules:
mario_bros = "OK"      # Can use letters, numbers, underscores
_princess = "OK"       # Can start with underscore
1up = "NOT VALID"      # Cannot start with number

# Operators

# Arithmetic
coins + bonus_coins    # Addition
lives - damage         # Subtraction
coins * multiplier     # Multiplication
points / divisor       # Division
coins // bowser        # Floor division
score % high_score     # Modulus (remainder)
mushroom ** power_up   # Exponentiation

# Comparison
mario == luigi         # Equal to
bowser != peach       # Not equal to
score > high_score    # Greater than
coins < target        # Less than
points >= threshold   # Greater than or equal to
lives <= max_lives    # Less than or equal to

# Logical
has_star and has_flower  # True if both are true
has_mushroom or is_fire  # True if at least one is true
not is_small             # Inverts boolean value

# String Operations

# String concatenation
character = "Mario"
action = "jumps"
message = character + " " + action  # "Mario jumps"

# String methods
name = "bowser"
name.upper()          # "BOWSER"
name.capitalize()     # "Bowser"
name.replace('b', 'w')  # "wowser"

# String formatting
character = "Mario"
coins = 99
# f-strings (Python 3.6+)
print(f"{character} collected {coins} coins!")

# String slicing
world = "World 1-1"
world[0]      # 'W'
world[0:5]    # 'World'
world[-3:]    # '1-1'

# Basic List Operations

# Creating lists
characters = ["Mario", "Luigi", "Peach", "Yoshi"]
inventory = ["Mushroom", 3, "Star", True]

# List operations
characters.append("Toad")     # Add to end
characters.pop()             # Remove and return last item
characters.insert(0, "Wario") # Insert at specific position
len(characters)             # Get length of list

# List slicing
mario_bros = characters[0:2]    # Get first two elements
reversed_chars = characters[::-1]  # Reverse the list

# Tuples

# Creating tuples (immutable lists)
coordinates = (3, 5)  # Mario's position in level
pipe_location = (100, 200, "Underground")
single_item = (1,)  # Need comma for single-item tuple

# Accessing tuple elements
x, y = coordinates  # Tuple unpacking
world_coords = pipe_location[:2]  # First two elements

# Common tuple operations

len(pipe_location)  # Number of elements
"Underground" in pipe_location  # Check if value exists
mario_pos = coordinates + (0,)  # Combine tuples

# Dictionaries

# Creating dictionaries

character_stats = {
    "Mario": {"lives": 3, "coins": 0, "power": "Fire"},
    "Luigi": {"lives": 3, "coins": 0, "power": "None"}
}

power_ups = {
    "Mushroom": "Super Mario",
    "Fire Flower": "Fire Mario",
    "Star": "Invincible"
}

# Accessing and modifying
mario_lives = character_stats["Mario"]["lives"]
power_ups["Ice Flower"] = "Ice Mario"  # Add new item
del power_ups["Mushroom"]  # Remove item

# Dictionary methods
all_powers = power_ups.keys()
power_effects = power_ups.values()
power_items = power_ups.items()  # Get key-value pairs

# Check if key exists
if "Star" in power_ups:
    print("Star power available!")

# Sets

# Creating sets (unique items only)
available_characters = {"Mario", "Luigi", "Peach", "Yoshi"}
unlocked_worlds = {1, 2, 3}

# Set operations
available_characters.add("Toad")
available_characters.remove("Peach")

# Set mathematics
player1_items = {"Mushroom", "Star", "Coin"}
player2_items = {"Flower", "Mushroom", "Shell"}

both_have = player1_items & player2_items  # Intersection
all_items = player1_items | player2_items  # Union
unique_to_player1 = player1_items - player2_items  # Difference

# Basic Functions

# Defining a function
def power_up(character):
    return f"{character} got a Super Star!"

# Function with default parameter
def collect_coins(amount=100):
    return f"Collected {amount} coins!"

# Function with multiple parameters
def calculate_score(coins, time_left):
    return coins * time_left

# Calling functions

power_up("Mario")              # "Mario got a Super Star!"
collect_coins()                # "Collected 100 coins!"
calculate_score(50, 120)       # 6000

# For Loops

# Basic for loop
for character in ["Mario", "Luigi", "Peach"]:
    print(f"{character} is ready to play!")

# Range-based for loop
for world in range(1, 9):
    print(f"Starting World {world}")

# Looping through dictionaries
for character, stats in character_stats.items():
    print(f"{character} has {stats['lives']} lives")

# Enumerate for index and value
for level, boss in enumerate(["Bowser Jr", "Kamek", "Bowser"], 1):
    print(f"Level {level} Boss: {boss}")

# While Loops

# Basic while loop
lives = 3
while lives > 0:
    print(f"Lives remaining: {lives}")
    lives -= 1

# Break and continue
coins = 0
while True:
    coins += 1
    if coins == 50:
        print("Got a 1-Up!")
        continue
    if coins >= 100:
        print("Extra life earned!")
        break

# Game-style loop
player_power = "Small"
while player_power != "Super":
    print("Looking for mushroom...")
    found_item = "Mushroom"  # Simulated item find
    if found_item == "Mushroom":
        player_power = "Super"
        print("Power up!")


# Track Mario's progress through a level
def play_level(level_number):
    player = {
        "character": "Mario",
        "power": "Small",
        "coins": 0,
        "position": 0
    }
    
    obstacles = [
        ("Goomba", 50),
        ("Pipe", 100),
        ("Koopa", 150),
        ("Flag", 200)
    ]
    
    for obstacle, position in obstacles:
        player["position"] = position
        
        if obstacle == "Flag":
            print("Level Complete!")
            break
            
        print(f"Encountered {obstacle} at position {position}")
        
        if player["power"] == "Small":
            print("Better find a mushroom!")

# Level progression system
worlds = {
    1: {"levels": 4, "unlocked": True},
    2: {"levels": 4, "unlocked": False},
    3: {"levels": 4, "unlocked": False}
}

for world_num, world_info in worlds.items():
    if not world_info["unlocked"]:
        continue
        
    print(f"World {world_num}")
    for level in range(1, world_info["levels"] + 1):
        print(f"Playing level {world_num}-{level}")
