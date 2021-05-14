import random
print("Hello there, looks like you are having trouble deciding what to eat. I'll help.")
cuisine_selection = {
    "Chinese":{"House of China", "Imperial Garden", "Golden Hunan"},
    "Japanese":{"Izumi", "Mizu", "Tokyo House"},
    "Mexican":{"Sr. Jalepeno", "Los Gallos", "El Vallarta"},
    "Indian":{"Cafe Indian", "Bombay Curry and Grill", "Nick & Mintu da dhaba"},
    "Pizza":{"Nicky's", "Bruno Brothers", "West Gate"},
    "Fast Food":{"Chic Fil A", "Panda Express", "Popeyes Chicken"},
    "Italian":{"Salvatores", "Scarsellas", "Nicolinni's"},
    "No Decide?":"Need to figure out what to do here."
}

cuisine_choice_responses = ["Excellent Choice. ", "Mmmmm... That's a delicious idea. ", "Oh yes. I'm getting fat tonight. ", "One of my favs. ", "My belly is happy. "]
random_response = random.choice(cuisine_choice_responses)

def welcome():
    try:
        cuisine_choice = int(input("Please select what type of cuisine you prefer: \n1 = Chinese\n2 = Japanese\n3 = Mexican\n4 = Indian \n5 = Pizza \n6 = Fast Food\n7 = Italian\n8 = I Don't Know!\nPlease enter a number: "))
        cuisine_choice -= 1
    except:
        print("\n\nWhoa there cowboy!!! You did not select a number. Please try again. ")
        welcome()

    if cuisine_choice >= 0 and cuisine_choice <= 8:
        print(random_response + "Have fun eating: "+list(cuisine_selection)[cuisine_choice])
    else:
        print("\n\nWell that wasn't an option! Select one of the options. Please try again.")
        welcome()
welcome()




#################
#OLD CODE

#Previous def welcome Contents
    # if cuisine_choice == "1":
    #     print(random_response+"You should eat at: "+random.choice(cuisine_selection["Chinese"]))
    # elif cuisine_choice == "2":
    #     print(random_response+"You should eat at: "+random.choice(cuisine_selection["Chinese"]))
    # elif cuisine_choice == "3":
    #     print(random_response+"You should eat at: "+random.choice(cuisine_selection["Chinese"]))
    # elif cuisine_choice == "4":
    #     print(random_response+"You should eat at: "+random.choice(cuisine_selection["Chinese"]))
    # elif cuisine_choice == "5":
    #     print(random_response+"You should eat at: "+random.choice(cuisine_selection["Chinese"]))
    # elif cuisine_choice == "6":
    #     print(random_response+"You should eat at: "+random.choice(cuisine_selection["Chinese"]))
    # elif cuisine_choice == "7":
    #     print(random_response+" You should eat at: "+random.choice(cuisine_selection["Chinese"]))
    # elif cuisine_choice == "8":
    #     my_random_choice = random.randint(1,8)
    #     if my_random_choice == 1:
    #         print(random_response+"You should eat at: "+random.choice(cuisine_selection["Chinese"]))
    #     elif my_random_choice == 2:
    #         print(random_response+"You should eat at: "+random.choice(cuisine_selection["Chinese"]))
    #     elif my_random_choice == 3:
    #         print(random_response+"You should eat at: "+random.choice(cuisine_selection["Chinese"]))
    #     elif my_random_choice == 4:
    #         print(random_response+"You should eat at: "+random.choice(cuisine_selection["Chinese"]))
    #     elif my_random_choice == 5:
    #         print(random_response+"You should eat at: "+random.choice(cuisine_selection["Chinese"]))
    #     elif my_random_choice == 6:
    #         print(random_response+"You should eat at: "+random.choice(cuisine_selection["Chinese"]))
    #     else:
    #         print(random_response+" You should eat at: "+random.choice(cuisine_selection["Chinese"]))
    # else:
    #     print("\033[1;32;47m You did not select a number. Please try again. ")
    #     #https://ozzmaker.com/add-colour-to-text-in-python/
    #     welcome()



    ####


    # print(test1)
# print(test2)
# print(test3)

# print(list(cuisine_selection)[0])
# print(test3)
# print(random.choice(cuisine_selection["Chinese"]))#choose a random value of Chinese
# print(random.choice(cuisine_selection["Japanese"]))#choose a random value of Japanese
# # print(random.choice(cuisine_selection.keys()))
# test1 = random.choice(list(cuisine_selection)) # Chooses a random choice of the Keys in cuisine selection
# test2 = random.choice(list(cuisine_selection)[0]) # Chooses a random letter choice of the word index at 0... aka Chinese.
# test3 = list(cuisine_selection)[1] # Makes the keys a list and selects the list item at index 1... aka Japanese.