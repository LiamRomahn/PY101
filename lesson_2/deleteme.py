def merge(x, y):
    lst = list(zip(x, y))

    new_list = []

    for nested in lst:
        for element in nested:
            new_list.append(element)
    
    return new_list


print(merge([1, 2, 3], [4, 5, 6]))



def third_occurence(string, character):

    counter = 0
    index = 0
    i = None

    for char in string:
        
        if char == character:
            counter += 1

        if counter == 3:            
            i = index
            break

        index += 1

    return i

print(third_occurence('aaa', 'a'))


x = [1, 2, 3]
repr_x = repr(x)
print(repr_x)  # Output: '[1, 2, 3]'
print(x)

