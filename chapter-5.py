# Exercise 1

print("Exercise 1\n")

#Making a dictionary 
infor = {
    'first_name' : 'Zach',
    'last_name' : 'Tonacao',
    'age' : 19, 
    'city' : 'Abu Dhabi'
}

#Printing the contents of the dictionary
print(infor['first_name'])
print(infor['last_name'])
print(infor['age'])
print(infor['city'])

#Exercise 2
print("Exercise 2\n")
#Dictionary of code descriptions
word = {
    'print' : 'displays the value of the variable',
    'input' : 'allows you to enter data in a program',
    'string' : 'is a group of characters or letters', 
    'variable' : 'is represented by a letter or a string and is assigned to a value',
    'constant' : 'is a variable whose value does not change'
}

#Printing of the description
print("The function print",{word['print']}, "\n")
print("The function input",{word['input']}, "\n")
print("A string",{word['string']}, "\n")
print("A variable",{word['variable']}, "\n")
print("A constant",{word['constant']}, "\n")

#Exercise 3
print("Exercise 3\n")
#Dictionary for code descriptions
word = {
    'print' : 'displays the value of the variable',
    'input' : 'allows you to enter data in a program',
    'string' : 'is a group of characters or letters', 
    'variable' : 'is represented by a letter or a string and is assigned to a value',
    'constant' : 'is a variable whose value does not change'
}

#Printing the key and values of the dictionary
for key, value in word.items():
    print(f"{key} {value}\n")

#Exercise 4
print("Exercise 4\n")
#Dictionary of Rivers
water = {
   'The Amazon River' : 'South America' ,
    'The Nile River' : 'Egypt',
    'The Ganges River' : 'India and Bangladesh'

}

#Prints the key and values together with a sentence.
for key, value in water.items():
    print(f"{key} runs through {value}\n")

#Prints only the key
for key in water.items():
    print({key}, "\n")

#Prints only the values
for value in water.items():
    print({value}, "\n")

#Exercise 5
print("Exercise 5\n")
#3 different variable with different dictionaries
dog = {'Dalmatian' : 'Chris'}
cat = {'Orange cat' : 'Garfield'}
chipmunk = {'Chimpmunk' : 'Alvin'}

#list made of the variables
pet = [dog, cat, chipmunk]

#prints the list which contains the dictionary
for boo in pet:
    print(boo, "\n")

