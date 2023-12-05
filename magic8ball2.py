import random

answers = [
    "Yes, definitely",
    "It is decidedly so",
    "Without a doubt", 
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now", 
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]

name = input("What's your name: ")

question = input("Ask your question: ")

random_index = random.randint(0, len(answers) - 1)
random_answer = answers[random_index]

print(name + " asks: " + question) 
print("Magic 8 Ball's answer: " + random_answer)