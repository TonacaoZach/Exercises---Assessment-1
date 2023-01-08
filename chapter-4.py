#Exercise 1

print ('Exercise 1 \n')
#Assigning a color to a variable
alien_color = 'green'

#checking if the color gets points
if alien_color == 'green':
    print("You have earned 5 points!\n")

#Exercise 1 (ver.2)

#Assigning a color to a variable
alien_color = 'red'

#checking if the color gets points
if alien_color == 'Green':
    print("You have earned 5 points!\n") 
    
#Exercise 2
print ('Exercise 2 \n')
#Assigning a color to a variable
alien_color = 'green'

#checking if the color gets an assigned amount of points
if alien_color == 'green':
    print("You have earned 5 points!") 
if alien_color in ['yellow', 'red']:
    print("You have earned 10 points\n")
    
#Exercise 2 (ver. 2)

#Assigning a color to a variable
aliencolor = 'red'

#checking the amount of points the color gets
if aliencolor == 'green':
    print("You have earned 5 points!") 
else:
    print("You have earned 10 points\n")

#Exercise 3
print ('Exercise 3 \n')
#Assigning a color to a variable
alien_color = 'red'

#checking the amount of points the color gets
if alien_color == 'green':
    print("You have earned 5 points!\n")
if alien_color == 'yellow':
    print("You have earned 10 points!\n")
if alien_color == 'red':
    print("You have earned 15 points!\n")

#Exercise 4
print ('Exercise 4 \n')
#Inputing a number for the variable
age = int(input("Enter your age:"))

#checking the variable through a if sentence if it matches a condition
if age < 2:
    print("You're a baby.")
elif age == 2 or age < 4:
    print("You're a toddler.")
elif age == 4 or age < 13:
    print("You're a kid.")
elif age == 13 or age < 20:
    print("You're a teenager.")
elif age == 20 or age < 65:
    print("You're an adult.")
else:
    print("You're an elder.")
    
#Exercise 5
print ('Exercise 5 \n')
#Adding strings to a list in a variable
fruits = ['banana', 'apple', 'cantaloupe', 'watermelon', 'mango']

#Asking user for their favourite fruit
fruit = input("What is your favorite fruit?: ")   

#Checking if their favourite fruit is in the list
if fruit == 'banana':
    print("Wow, you like bananas!")   
if fruit == 'apple':
    print("Wow, you like apples!")  
if fruit == 'cantaloupe':
    print("Wow, you like cantaloupes!")  
if fruit == 'watermelon':
    print("Wow, you like watermelons!")  
if fruit == 'mango':
    print("Wow, you like mangoes!") 
else:
    print("Your fruit is not on my list of favourites :P")

 
    

