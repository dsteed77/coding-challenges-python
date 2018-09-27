###
# This string manipultation file contains the following fuctions:
# Parenthesis_Checker
# Reverse_Words 
# Permutations_Of_String
# Longest_Palindrome_String
# Recursively_Remove_Adjacent_Duplicates 
# Check_if_string_is_rotated_by_two_places
# Roman_Number_to_Integer
# Anagram Longest_Common_Substring 
# Remove_Duplicates Form_Palindrome
# Longest_Distinct_Characters_String
# Implement_Atoi 
# Implement_strstr
# Longest_Common_Prefix
# Subarray_With_Sum
###

def Reverse_Words(): #this is the function definition so we can break our coding challenges in different modules
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


