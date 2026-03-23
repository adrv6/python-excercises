
item=['🍔 Cheeseburger', '🍟 Fries', '🥤 Soda', '🍦 Ice Cream', '🍪 Cookie']

def get_item(x):
  if x == 1:
    return "🍔 Cheeseburger"
  elif x == 2:
    return "🍟 Fries"
  elif x == 3:
    return "🥤 Soda"
  elif x == 4:
    return "🍦 Ice Cream"
  elif x == 5:
    return "🍪 Cookie"
  else:
    return "Error! try again"

def welcome():
  print('Welcome to WcDonalds!')
  print("Here is our menu:")
  print('1 🍔 Cheeseburger')
  print('2 🍟 Fries')
  print('3 🥤 Soda')
  print('4 🍦 Ice Cream')
  print('5 🍪 Cookie')

welcome()

option =int(input("What would you like to order? "))
print(get_item(option))
