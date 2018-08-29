from string_manipulations import *

def printMainMenu(function_cat_list):
    print('\nHello, This is a console app I made to help prepare for interviews! \nMain Menu: \n ')

    i=0
    for cat in function_cat_list:
        print((i+1) , ' ' ,  function_cat_list[i])
        i+=1

def userSelection(function_cat_list):
    invalid_choice = True
    while invalid_choice:
        #print(len(function_cat_list)) #DEBUG
        user_selection = input('\nPlease select an number from the menu: \n')

        try:
            val = int(user_selection)
        except ValueError:
            print("That's not a number!")

        if val <= len(function_cat_list) and val > 0:
            invalid_choice = False #meaning that if valid unput is given, it will work!
        else:
            print('\nPlease select a valid input.')        

    #print(user_selection)#DEBUG - Remove. 
    
    print('\nYou selected - ' + function_cat_list[int(user_selection)-1])
    return user_selection

def listToDict(function_cat_list):
    i=0
    select_dict_options = {}

    for cat in function_cat_list:
        select_dict_options[i+1] = function_cat_list[i]
        i+=1
        
    print(select_dict_options)

def subMenu(user_selection, ):
    listToDict