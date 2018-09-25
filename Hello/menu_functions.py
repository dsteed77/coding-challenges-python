import String_Manipulation

function_cat_list = [
    ['String Manipulation', "Parenthesis Checker", "Reverse Words", 
    "Permutations Of String", "Longest Palindrome String", "Recursively Remove Adjacent Duplicates", 
    "Check if string is rotated by two places", "Roman Number to Integer", "Anagram", "Longest Common Substring", 
    "Remove Duplicates", "Form Palindrome", "Longest Distinct Characters String", "Implement Atoi", 
    "Implement strstr", "Longest Common Prefix", "Subarray With Sum"], 

    ['Arrays', "Finding middle element in a linked list", "Reverse a linked list", "Rotate a Linked List", 
    "Reverse a Linked List in groups of given size", "Detect Loop in linked list", "Remove loop in Linked List", 
    "nth node from end of linked list", "Flattening a Linked List", "Merge two sorted linked lists", 
    "Intersection point of two Linked Lists", "Pairwise swap of a linked list", "Add two numbers represented by linked lists", 
    "Check if Linked List is Palindrome", "Implement Queue using Linked List", "Implement Stack using Linked List", 
    "Given a linked list of 0s, 1s and 2s, sort it", "Delete without head pointer"], 

    ['Linked Lists', "Next larger element", "Queue using two Stacks", "Stack using two queues", "Get minimum element from stack", 
    "LRU Cache", "Circular tour", "First non-repeating character in a stream", "Rotten Oranges"],
    
    ['Stack/Queue'], 
    ['Tree'], 
    ['Recursion'],
    ['Hashing'],
    ['etc.']
    ]

def printMainMenu():
    print('\nHello, This is a console app I made to help prepare for interviews! \nMain Menu: \n ')

    i=0
    for cat in function_cat_list:
        print((i+1) , ' ' ,  function_cat_list[i][0])
        i+=1

def userSelection():
    invalid_choice = True
    while invalid_choice:
        #print(len(function_cat_list)) #DEBUG
        user_selection = input('\nPlease select a number from the menu: \n')
        #print(user_selection)
        val = 0
        try:
            val = int(user_selection)
        except ValueError:
            print("That's not a number!")

        if val <= len(function_cat_list) and val > 0:
            invalid_choice = False #meaning that if valid unput is given, it will work!
        else:
            print('Please select a valid input.')        

    #print(user_selection)#DEBUG - Remove. 
    
    print('\nYou selected - ' + function_cat_list[val-1][0])
    return val
    
def printSubMenu(user_selection):
    i=0
    for sub_cat in range(len((function_cat_list[user_selection-1]))-1):
        i+=1
        print((i) , ' ' ,  function_cat_list[user_selection-1][i])    

    invalid_choice = True
    while invalid_choice:
        #print(len(function_cat_list)) #DEBUG
        user_selection_sub = input('\nPlease select a number from the sub-menu: \n')
        val = 0

        try:
            val = int(user_selection_sub)
        except ValueError:
            print("That's not a number!")

        print (len(function_cat_list[user_selection - 2]))
        if val < len(function_cat_list[user_selection - 1]) and val > 0:
            invalid_choice = False #meaning that if valid unput is given, it will work!
        else:
            print('\nPlease select a valid input.')        

    #print(user_selection)#DEBUG - Remove. 
    print('\nYou selected - ' + function_cat_list[user_selection - 1][val])
    return val

from String_Manipulation import *
def executeFunction(category, function):
    function_name = function_cat_list[category-1][function]
    category_name = function_cat_list[category-1][0]

    print('Executing ' + function_name)
    print('From Category: ' + category_name + '\n')

    function_name = function_name.replace(' ', "_")
    category_name = category_name.replace(' ',"_")

    #Assuming module String_Manipulation with method function:
    #String_Manipulation.Reverse_Words()
    function_to_call = getattr(category_name, function_name)
    #method_to_call = getattr(foo, 'bar')
    function_to_call()
