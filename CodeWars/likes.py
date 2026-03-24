# Codewars - 6 kyu
# https://www.codewars.com/kata/5266876b8f4bf2da9b000362
# 
# Implement a function that takes an array of names and returns
# the display text for a "likes" system.

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        other = len(names) - 2
        return f"{names[0]}, {names[1]} and {other} others like this"