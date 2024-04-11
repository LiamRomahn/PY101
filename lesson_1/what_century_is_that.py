def century(integer):
    year = str(integer)
    
    if len(year) == 1:
        return '1st'
    
    century_number = year[0:2] if year.endswith('00') else str(int(year[0: len(year) - 2]) + 1)
    suffix = ''
            
    match century_number[-1]:
        case '1':
            suffix = 'st'
        case '2':
            suffix = 'nd'
        case '3':
            suffix = 'rd'
        case _:
            suffix = 'th'

    return century_number + suffix







