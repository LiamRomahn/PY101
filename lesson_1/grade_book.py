def get_grade(x, y, z):
    mean = (x + y + z) / 3
    if mean <= 100 and mean >= 90:
        return 'A'
    elif mean < 90 and mean >= 80:
        return 'B'
    elif mean < 80 and mean >= 70:
        return 'C'
    elif mean < 70 and mean >= 60:
        return 'D'
    else:
        return 'F'
    
print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True
    