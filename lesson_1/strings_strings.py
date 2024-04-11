def stringy(integer):
    if integer < 1:
        return 'Input an integer greater than 0.'
    string = '1'
    for number in range(integer - 1):
        if number % 2 == 0:
            string += '0'
        else:
            string += '1'
   
    return(string)
print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True

