# Exercise 1

print("\nExercise 1\n")

#Adding strings to a variable.
hel = ("Hello, how are you")
#Using the variable instead of a full setence
print(hel)

#Same as the first 
hel = ("I'm good.")
#same as the one shown above, \n is a code for adding a new line
print(hel,"\n")

#Exercise 2

print("\nExercise 2\n")

#Adding strings to a variable
author = ("Sova")
quote = ("“If your not a good shot today don't worry there are other ways to be useful.”")

#Using variable and string to form a sentence
print(author, "once said", quote,"\n")

#Exercise 3

print("\nExercise 3\n")

name = ("Zak")

#\n \t Adds a new line and tab respectively
print("Z\ta\nk\t")

#Strips the text according to function
print(name.lstrip())
print(name.rstrip())
print(name.strip(), "\n")

#Exercise 4

print("Exercise 4\n")

#inputed number
numb = 22
#printing inputed number with a sentence
print("My favorite number is", numb, "\n")

#Exercise 5

print("\nExercise 5\n")

#The numbers given 
balance = 50
usb = 6

#Equation to find the change of the given numbers
total = balance//usb
how = total*usb
change = balance - how

print("The girl can buy", total, "USB sticks and she will have", change, "as change.")