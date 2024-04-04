# Opening it with a { (curly-brace).
email = {
    "From": "john_smith@gmail.com",
    "to": "david@david.com",
    "Subject": "Hello David"
};

print(email["From"])

messages = [
  {"to": 'Sun', "from": 'Moon', "message": 'Hi!'},
  {"to": 'Moon', "from": 'Sun', "message": 'What do you want Sun?'},
  {"to": 'Sun', "from": 'Moon', "message": "I'm awake!"},
  {"to": 'Moon', "from": 'Sun', "message": 'I can see that Sun.'}
];

print (messages [2] ['to'])