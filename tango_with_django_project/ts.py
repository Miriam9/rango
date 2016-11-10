def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    trans = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si',
             '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu', '10': 'shi'}

    chinese_num = ''

    for i in us_num:
        if int(us_num) is <= 11:
            chinese_num = trans[us_num]


    return chinese_num


print(convert_to_mandarin(5))

