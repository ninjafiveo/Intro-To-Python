import random
# cuisineSelection = {
#     "Chinese":{"House of China", "Imperial Garden", "Golden Hunan"},
#     "Japanese":{"Izumi", "Mizu", "Tokyo Housu"},
#     "Mexican":{"Sr. Jalepeno", "Los Gallos", "El Vallarta"},
#     "Indian":{"Cafe Indian", "Bombay Curry and Grill", "Nick & Mintu da dhaba"},
#     "Pizza":{"Nicky's", "Bruno Brothers", "West Gate"},
#     "Fast Food":{"Chic Fil A", "Panda Express", "Popeyes Chicken"},
#     #"Italian":{"Salvatores", "Scarsellas", "Nicolinni's"},
# }
# print(cuisineSelection["Chinese"][0][1])

# val = random.choice(list(cuisineSelection.items()))
# print(val)

chinese_food = ["House of China", "Imperial Garden", "Golden Hunan", "Main Moon", "Chinatown Inn"]
japanese_food = ["Izumi", "Mizu", "Tokyo House", "Sakura", "Asuka"]
mexican_food = ["Sr. Jalepeno", "Los Gallos", "El Vallarta"]
indian_food =["Cafe Indian", "Bombay Curry and Grill", "Nick & Mintu da dhaba"]
pizza_food =["Nicky's", "Bruno Brothers", "West Gate"]
fast_food = ["Chic Fil A", "Panda Express", "Popeyes Chicken"]
italian_food = ["Salvatores", "Scarsellas", "Nicolinni's"]

cuisine_choice_responses = ["Excellent Choice. ", "Mmmmm... That's a delicious idea. ", "Oh yes. I'm getting fat tonight. ", "One of my favs. ", "My belly is happy. "]

random_response = random.choice(cuisine_choice_responses)

# print(random.choice(chinese_food))
def welcome():
    print("Hello there, looks like you are having trouble deciding what to eat.")
    cuisine_choice = input("Please select what type of cuisine you prefer: \n1 = Chinese\n2 = Japanese\n3 = Mexican\n4 = Indian \n5 = Pizza \n6 = Fast Food\n7 = Italian\n8 = I Don't Know!\nPlease enter a number: ")
    if cuisine_choice == "1":
        print(random_response+"You should eat at: "+random.choice(chinese_food))
    elif cuisine_choice == "2":
        print(random_response+"You should eat at: "+random.choice(japanese_food))
    elif cuisine_choice == "3":
        print(random_response+"You should eat at: "+random.choice(mexican_food))
    elif cuisine_choice == "4":
        print(random_response+"You should eat at: "+random.choice(indian_food))
    elif cuisine_choice == "5":
        print(random_response+"You should eat at: "+random.choice(pizza_food))
    elif cuisine_choice == "6":
        print(random_response+"You should eat at: "+random.choice(fast_food))
    elif cuisine_choice == "7":
        print(random_response+" You should eat at: "+random.choice(italian_food))
    elif cuisine_choice == "8":
        
        print(random_response+" You should eat at: "+random.choice(italian_food))
    else:
        print("\033[1;32;47m You did not select a number. Please try again. ")
        #https://ozzmaker.com/add-colour-to-text-in-python/
        welcome()
welcome()