height = int(input("What's your height? "))

credit = int(input("How many credit you have? "))

if height >= 137 and credit >= 10:
  print("Enjoy the ride!")
elif height < 137 and credit >= 10:
  print("You are not tall enough to ride")
elif height >= 137 and credit < 10:
  print("You don't have enough credit")
else:
  print("You cannot ride.")
