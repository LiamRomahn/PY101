def clean_up(string):
    
    lst_string = list(string)
    new_string = ''
    
    index = 0
    for element in lst_string:
        
        if element.isalpha():
            new_string += element     
        
        elif (not lst_string[index].isalpha()) and (index == len(lst_string) - 1): #fix for out of index error
            new_string += ' '
        
        elif (not lst_string[index].isalpha()) and (not lst_string[index + 1].isalpha()): #passes when there are
            pass                                                                          #2 non-alphas in a row
        
        else:
            new_string += ' '
        
        index += 1
    
    return new_string