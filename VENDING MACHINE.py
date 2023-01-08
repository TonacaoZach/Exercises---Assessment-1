totalsnack = 0
totaldrink = 0

def printMain(): #prints main menu
    print("\t\t | MAIN MENU | \n\t")
    print("\t\t [1] DRINKS \t\n")
    print("\t\t [2] SNACKS \t\n")  
        
def printDrinks():#prints lists of drinks
    
    totaldrink = 0 #default value in the beginning
    
    print("\n\t| DRINKS |\n")  
    print("\t 1. Pepsi (4.00) \n\t 2. 7 up (4.00) \n\t 3. Mountain Dew (4.00) \n\t 4. Oasis Water (1.00) \n\t 5. Main Menu\n")
    while True:
        
        answer = input("Select a drink: ") #asks for a user input for the snack chosen
        
        if answer == "1":
            print("Pepsi (4.00) has been added.")
            totaldrink = totaldrink + 4.00
        elif answer == "2":
            print("7 up (4.00) has been added.")
            totaldrink = totaldrink + 4.00
        elif answer == "3":
            print("Mountain Dew (4.00) has been added.")
            totaldrink = totaldrink + 4.00
        elif answer == "4":
            print("Oasis Water (1.00) has been added.")
            totaldrink = totaldrink + 1.00
        elif answer == "5":
            print("Your current total due is", totaldrink)
            break
        else:
            print("Input is invalid")
    return totaldrink #this returns the value of totalsnack

def printSnacks():#prints lists of snacks
    
    totalsnack = 0 #default value in the beginning
    
    print("\n\t | SNACKS |\n") 
    print("\t 1. Reese's (2.50) \n\t 2. Chips Ahoy (3.00) \n\t 3. Takis (4.00) \n\t 4. Twix (3.50)\n\t 5. Main Menu\n")
        
    while True:
        
        answer = input("Select a snack: ") #asks for a user input for the snack chosen
        
        if answer == "1":
            print("Reese's (2.50) has been added.")
            totalsnack = totalsnack + 2.50
        elif answer == "2":
            print("Chips Ahoy (3.00) has been added.")
            totalsnack = totalsnack + 3.00
        elif answer == "3":
            print("Takis (4.00) has been added.")
            totalsnack = totalsnack + 4.00
        elif answer == "4":
            print("Twix (3.50) has been added.")
            totalsnack = totalsnack + 3.50
        elif answer == "5":
            print("Your current total due is", totalsnack)
            break 
        else:
            print("Input is invalid")
            
    return totalsnack #this returns the value of totalsnack

def printPay(totalsnack, totaldrink):
    
    amount = totalsnack + totaldrink #the total of the drinks and snacks amount combined
    print("Your total amount is", amount)
    
    while True:
         cash = float(input("Enter your cash: ")) #Asks the user to input their money
         print("You have given", cash)
         change = cash - amount #formula for the change the user gets
         
         if cash < amount: #if statement checking if the cash given is less than the amount needed to pay
                print("Insufficient funds.")
         else:
                print("Your change is", change) #prints the amount of money returned to the user
                print("Thank you for using this vending machine!")
                break

#Actual Vending Machine
amount = 0

printMain() #the menu being printed

while True:
    
        choice = input("Enter '1' to check our available drinks.\nEnter '2' to check our available snacks.\nEnter '3' to pay.\nENTER THE NUMBER: ") 

        if choice == "1":
            totaldrink = printDrinks() #drink Menu Printed
        elif choice == "2":
            totalsnack = printSnacks() #snack Menu Printed
        elif choice == "3":
            printPay(totalsnack, totaldrink)
            break
        else:
            print("Input is Invalid.")
            
        
            
            


    

      
            
        




