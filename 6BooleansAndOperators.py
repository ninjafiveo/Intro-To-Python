#Booleans are true or false.
import getpass #Hides passwords typed

def check_boolean():
    print(10 > 9) # 10 is greater than 9 = True
    print(10 == 9) # 10 is equal to 9 = False
    print(10 < 9) # 10 is less than 9 = False
#check_boolean()


def boolean_condition():
    username = input("Please enter your username: ")
    # password = input("Please enter your password: ")
    password = getpass.getpass("Please enter your password: ") #using the getpass import to hide password. 
    if username == "admin" and password == "mcctcrocks":
        print("You have been granted access.")
    else:
        print("Your username and/or password are incorrect.")
        try_again =  input("Would you like to try again? y or n ")
        if try_again == "y":
            boolean_condition()
        else:
            print("Have a nice day.")

# print("Welcome to Nerd Inc.")
# boolean_condition()

####
####
#Operators
def py_operators():
     x = 7 # = is the assignment operator
     y = 5
     print(x+y) #Addition
     print(x-y) #Subtraction
     print(x*y) #Multiplication
     print(x/y) #Division
     print(x%y) #Modulus... the remainder.
     print(x**y) #Exponentiation
     print(x//y) #Floor Division (Rounds Down.)
# py_operators()

def py_assignment_ops():
    x = 5 #Assigns 5 to x
    print(x)
    x += 3 #Adds 3 to x. (5+3=8) 
    print(x)
    x-=1 #Subtracts 1 from x
    print(x)
    x *= 6 #Multiplies x by 6
    print(x)
    x /= 3 # Divides x by 3
    print(x)
    x %= 3 # Remainder of x divided by 3 (14/3 = 4 remainder 2)
    print(x)
    print("You can find more here: https://www.w3schools.com/python/python_operators.asp")

#py_assignment_ops()
    



