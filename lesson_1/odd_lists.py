def oddities(lst):
    return lst[::2]
def evens(lst):
    return lst[1::2]

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True
print(evens([1,2,3,4,5,6]))

str1 = '012345678'
print(str1[0::2])

