import random

question = input("Question: ")

replies = random.randint(1,9)

print("Magic 8 Ball: ")

if replies == 1:
  print("Yes - Definately")
elif replies == 2:
  print("It is decidedly so")
elif replies == 3:
  print("Without a doubt")
elif replies == 4:
  print("Reply hazy, try again")
elif replies == 5:
  print("Ask again later")
elif replies == 6:
  print("Better not tell you now")
elif replies == 7:
  print("My sources say no")
elif replies == 8:
  print("Outlook not so good")
else:
  print("Very doubtful")
print('Magic 8 Ball:  ' + print)