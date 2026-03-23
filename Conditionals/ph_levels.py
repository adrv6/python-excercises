ph = int(input("PH level (0-14): "))
if ph > 7:
  print("basic")
elif ph < 7:
  print("Acidic")
else:
  print("Neutral")