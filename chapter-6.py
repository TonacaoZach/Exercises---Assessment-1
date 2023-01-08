#Exercise 1

print("\nExercise 1\n")

#While loop repeates the code until the loop is broken
while True:
    
    #asks the user the input and ingredient
    pizza = input("Enter any ingredient to put on the pizza. Enter 'QUIT' if you want to stop adding toppings: ")
    
    #If statement to check if the input matches the conditions for it to break
    if pizza == 'QUIT':
        print("Enjoy your pizza!")
        break
   #If statement if the first condition wasn't met
    else:
        print(pizza, "has been added to your pizza.")
        continue

#Exercise 2

print("\nExercise 2\n")

#While loop repeating the code unless broken
while True:
    
    #Asks user to add an input 
    age = int(input("Hi! Welcome to the movie theatre, how old are you?: "))
    
    #if statement to check which of the conditions does the user input it matches
    if age < 3:
        print(f"oh, You are {age} years old? Here is your ticket, it is free.")
        break
    elif age >= 3 and age <= 12:
        print(f"oh, You are {age} years old? Here is your ticket, it is $10.")
        break
    else:
        print(f"oh, You are {age} years old? Here is your ticket, it is $15. ")
        break

"""#Exercise 3

print("\nExercise 3\n")

#Contineously repeats the phrase "WOW THIS IS!"
while True:
    print("Wow this is!")"""


#Exercise 4

print("\nExercise 4\n")

#list of sandwiches
sandwhichs = ['BLT', 'Egg', 'Club']
#List without content for finished sandwiches
finished_sandwhiches = []

#While loop to repeate until coditions have been met or broken
while sandwhichs:
    
    #making a new varibale to store the items removed from the list
    current_sandwhich = sandwhichs.pop()
    print(f"I am working on your {current_sandwhich} sandwhich.")
    finished_sandwhiches.append(current_sandwhich)

print("\n\n")

#Printing the finish product of the loop
for sandwhich in finished_sandwhiches:
    print(f"I am going to eat a {sandwhich} sandwhich")
    

#Exercise 5

print("\nExercise 5\n")

sandwich_orders = ['turkey', 'pastrami', 'tuna', 'pastrami', 'pastrami', 'roast beef']
finished_sandwiches = []

print (sandwich_orders)

print("Sorry, the deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print("I made your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

print("\nThese sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)




