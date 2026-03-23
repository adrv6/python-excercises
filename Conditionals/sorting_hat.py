Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")

answer_1 = int(input("Answer: "))

if answer_1 == 1:   
    Gryffindor += 1
    Ravenclaw += 1
elif answer_1 == 2:   
    Hufflepuff += 1 
    Slytherin += 1
else:
  print("Wrong input")

print("When I'm dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")

answer_2 = int(input("Answer: "))

if answer_2 == 1:
  Hufflepuff = + 2
elif answer_2 == 2 :
  Slytheryn = + 2
elif answer_2 == 3 :
  Ravenclaw = + 2
elif answer_2 == 4:
  Gryffindor = + 2
else:
  print("Wrong input.")

print("which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

answer_3 = int(input("Answer: "))
if answer_3 == 1:
  Slytherin = + 4
elif answer_3 == 2:
  Hufflepuff = + 4
elif answer_3 == 3:
  Ravenclaw = + 4
elif answer_3 == 4:
  Gryffindor = + 4
else:
  print("Wrong input.")

print("Gryffindor: ", Gryffindor)
print("Ravenclaw:  ", Ravenclaw)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin)

#Bonus:

if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
  print('🦁 Gryffindor!')
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
  print('🦅 Ravenclaw!')
elif Hufflepuff >= Slytherin:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')
