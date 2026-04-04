#CodeWars - 7 kyu
#Find the shortest word in a String

def find_short(s):
    return min(len(word) for word in s.split())
