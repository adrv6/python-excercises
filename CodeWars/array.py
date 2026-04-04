#CodeWars - 6 kyu
#Array diff- removes from 'a' anny elements that appear in 'b'

def array_diff(a, b):
    result = []
    for element in a:
        if element not in b:
            result.append(element)
    return result
