#Exercise 1

print("\nExercise 1\n")

#defines a keyword to define a function
def displaym():
    
    #adding strings to a variable
    msg = "So this is define function."
    
    #printing the variable
    print(msg)

#The function
displaym()

#Exercise 2 

print("\nExercise 2\n")

#defining a keyword with the function
def favbook(title):
    
    #prints the f-string with function
    print(f"{title} is the book that I like.")
    
#The function and its content
favbook('Romeo and Juliet')

#Exercise 3 

print("\nExercise 3\n")

#defining keyword with variable
def shirt(size, message):
    
    #printing the strings with variable
    print(f"I am going to make a {size} t-shirt")
    print(f"It will say {message}\n")

#contents of the variable
shirt('Large', 'CheeseBurger')
shirt(size = 'Medium', message = 'CheeseBurger')

#Exercise 4 

print("\nExercise 4\n")

#Defining the keyword, with the content of the variables
def shirt(size = 'Large', message = 'I love Python'):
    
    #printing the strings with the variables
    print(f"I am going to make a {size} shirt.")
    print(f"It will say {message}.\n")
    
#the function and content
shirt()
shirt(size = 'medium')
shirt('Extra Large', 'Amazeballs')

#Exercise 5

print("\nExercise 5\n")

#defines a keyword with function one with content the other without
def cities(city, country = 'United Arab Emirates'):
    
    #printing using f-string using the variable
    print(f"{city.title()} is located in {country.title()}.\n")

#The function and its contents    
cities('abu dhabi')
cities(city = 'Manila', country = 'philippines')
cities('dubai')
