import random
cuisine_selection = {
    "Chinese":("House of China", "Imperial Garden", "Golden Hunan"),
    "Japanese":("Izumi", "Mizu", "Tokyo House"),
    "Mexican":("Sr. Jalepeno", "Los Gallos", "El Vallarta"),
    "Indian":("Cafe Indian", "Bombay Curry and Grill", "Nick & Mintu da dhaba"),
    "Pizza":("Nicky's", "Bruno Brothers", "West Gate"),
    "Fast Food":("Chic Fil A", "Panda Express", "Popeyes Chicken"),
    "Italian":("Salvatores", "Scarsellas", "Nicolinni's"),
}
cuisine_choice_responses = ["Excellent Choice. ", "Mmmmm... That's a delicious idea. ", "Oh yes. I'm getting fat tonight. ", "One of my favs. ", "My belly is happy. "]
random_response = random.choice(cuisine_choice_responses)
def welcome():
    print("Hello there, looks like you are having trouble deciding what to eat. I'll help.")
    cuisine_choice = int(input("Please select what type of cuisine you prefer: \n1 = Chinese\n2 = Japanese\n3 = Mexican\n4 = Indian \n5 = Pizza \n6 = Fast Food\n7 = Italian\n8 = I Don't Know!\nPlease enter a number: "))
    cuisine_choice -= 1
    if cuisine_choice >= 1 and cuisine_choice <= 8:
        print(random_response + "Have fun eating: "+list(cuisine_selection)[cuisine_choice])
    else:
        print("\033[1;32;47m You did not select a number. Please try again. ")
        welcome()
welcome()