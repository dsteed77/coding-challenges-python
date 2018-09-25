['String Manipulation', "Parenthesis Checker", "Reverse Words", 
    "Permutations Of String", "Longest Palindrome String", "Recursively Remove Adjacent Duplicates", 
    "Check if string is rotated by two places", "Roman Number to Integer", "Anagram", "Longest Common Substring", 
    "Remove Duplicates", "Form Palindrome", "Longest Distinct Characters String", "Implement Atoi", 
    "Implement strstr", "Longest Common Prefix", "Subarray With Sum"]

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


