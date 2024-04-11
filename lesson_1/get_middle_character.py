def center_of(string):
    middle_string = (len(string) // 2) - 1
    
    if len(string) == 1:
        return string
    elif len(string) % 2 == 0:
        return string[middle_string: middle_string + 2]
    else:
        return string[middle_string + 1]




print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True