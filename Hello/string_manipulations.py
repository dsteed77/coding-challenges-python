def reverseStringWords(): #this is the function definition so we can break our coding challenges in different modules
    rev_string = input('Enter string to reverse(words):')

    print('You entered: ' + rev_string)

    string_list = rev_string.split()
    new_string = ''
    i_length = len(string_list) - 1

    for string in string_list:
        new_string+=string_list[i_length]
        new_string+=' '
        i_length-=1
    
    print('Reversed String: ' + new_string)


