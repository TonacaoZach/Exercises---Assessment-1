#Exercise 1

print("\nExercise 1\n")

#List of names
name = ['Zach', 'Zack', 'Zak', 'Zac', 'Jak']

#Printing list by order of index
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4], "\n")

#Exercise 2

print("\nExercise 2\n")

#list of names
name = ['Zach', 'Zack', 'Zak', 'Zac', 'Jak']

#Printing list by order of index with added setences
print("\nI hope your good,",name[0])
print("\nI hope your good,",name[1])
print("\nI hope your good,",name[2])
print("\nI hope your good,",name[3])
print("\nI hope your good,",name[4], "\n")

#Exercise 3

print("Exercise 3\n")

#list of cars
transp = ['maserati', 'buggati', 'ferrari']

#printing list of cars
print("\nI would like to own a ", transp[0])
print("\nI would like to own a ", transp[1])
print("\nI would like to own a ", transp[2], "\n")

#Exercise 4

print("Exercise 4\n")

#List of people
guest = ['Dianne', 'Sana', 'John Mayer']

#Using index to print strings from the list
print("Would you like to go to dinner with me,", guest[0], "?\n")
print("Would you like to go to dinner with me,", guest[1], "?\n")
print("Would you like to go to dinner with me,", guest[2], "?\n")

#Exercise 5

print("Exercise 5\n")

#List of people
guest = ['Dianne', 'Sana', 'John Mayer']

#printing the list of people
print("\nWould you like to go to dinner with me,", guest[0], "?")
print("\nWould you like to go to dinner with me,", guest[1], "?")
print("\nWould you like to go to dinner with me,", guest[2], "?\n")

#using f-strings to use printing the index
print(f"\nOh no! {guest[2]} can't come.\n")

#code for storing the removed guest from the list
popped_guests = guest.pop(2)

#Asking user to add another person
new = input("Who would you like to invite?: \n")

#Adding the new person to the list
guest.append(new)

#printing the new list
print("\nWould you like to go to dinner with me,", guest[0], "?")
print("\nWould you like to go to dinner with me,", guest[1], "?")
print("\nWould you like to go to dinner with me,", guest[2], "?\n")

#Exercise 6

print("\nExercise 6\n")

#list of people
guest = ['Dianne', 'Sana', 'John Mayer']

#printing a sentence
print("\nOh no! My new dining table won't be able to arrive on time, sorry I can only invite two people!\n")

#Removing a person from the list
popped_guest = guest.pop(2)

#Using the code that stored the removed guest to display a sentence
print(f"Sorry, {popped_guest}, I can't invite you anymore.\n")

#Printing the people left in the list
print("\nYou're still invited", guest[0])
print("\nYou're still invited", guest[1], "\n")

#deletes all the guest
del guest[:]

#prints all the list "guest"
print(guest, "\n")

#Exercise 7

print("\nExercise 7\n")

#list of famous cities or countries
place = ['Seoul','New York' ,'Switzerland', 'Tokyo', 'Maldives']

#prints the list
print(place, "\n")

#prints the sorted alphabetical list
print(sorted(place))
print(place, "\n")

#prints the reversed sorted alphabetical list
print(sorted(place, reverse=True))
print(place, "\n")

#prints the sorted alphabetical list that was previously reversed
print(place.reverse())
print(place, "\n")


#prints the list sorted alphabetically
place.sort()
print(place)

#prints the list sorted alphabetically reversed
place.sort(reverse=True)
print(place)




