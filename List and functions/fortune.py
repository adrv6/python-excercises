
import random #generate the random function

#call a function with random.randint
def fortune():
  num = random.randint(1,8)
  if num == 1:
    print('Dont pursue happines - create it')
  if num == 2:
    print ('All things are difficult before they are easy')
  if num == 3:
    print('The early bird gets the worm, but the second mouse gets the cheese')
  if num == 4:
    print('Someone in your life needs a letter from you')
  if num == 5:
    print('Dont just think, act!')
  if num == 6:
    print('Your heart will skip a beat')
  if num == 7:
    print('The fortune you search for is in another cookie')
  else:
    print('Help! I am being held prisioner in a chinese bakery!!')


#call the function 3 times
fortune()