def twice(integer):
    string = str(integer)
    
    if len(string) % 2 != 0:
        return integer * 2
    
    elif string[0: int(len(string) / 2)] == string[int(len(string) / 2)::]:
        return integer
    
    else:
        return integer * 2





print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True