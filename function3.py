#def first_name():
 #   print(input ("what's your name?"))

#first_name()

#def last_name():
#    print (input ("what's your last name?"))

#last_name()

#print ("OK, so your name is {first_name} {last_name} . I got it")

def first_name():
    return input("What's your name? ")

def last_name():
    return input("What's your last name? ")

user_first_name = first_name()
user_last_name = last_name()

print(f"OK, so your name is {user_first_name} {user_last_name}. I got it.")


