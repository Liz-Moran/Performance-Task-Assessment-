#Purpose: This program helps the user keep track of their money by storing transactions and showing their balance and totals for a category they choose to spend their money on.  
transactions=[]  #This list stores every transaction as [amount, category] 

#Student-developed procedure:
#Function I made to add a transaction to the list. It uses parameters (amount and category) and prints out user inputs.

def add_transaction(amount, category):
    transactions.append([amount, category]) # This stores the data (sequencing)
    #This checks if the amount entered is negative or positive (selection)
    if amount < 0: 
        print("Balence updated (expense added).")
    else:
        print("Balence added.")


# Intro messages for a better user experience
print("Mini Money Manager")
print("==================")
print("Welcome to Mini Money Manager, where you can track your money.")
print("Enter postive numbers to add to your balence and negative numbers for expenses.")
print("Type 'stop' when done.\n")

#Main loop that keeps running while asking users for transactions until they type "stop" to end it.
while True:   
    user_input = input("Enter amount: ")

    if user_input.lower()=="stop": #Condition to exit loop once user wants to stop entering transactions
        break


    try:        #Try to convert the input into a number 
        amount = float(user_input)
    except:
        print("Not a number. Please try again.")
        continue   #Sends the user back to the beginning of the loop
        
    #Asks the user what the money was for
    category= input("What is this money for?: ")
    add_transaction(amount, category)

    # Calculates the running total balance (iteration)
    total = 0
    for t in transactions:    #Loop through the list
        total +=t[0]

    #Shows the user the updated balance
    print("Current balance: $", total)
    print("--------------------------")

#After the user is done, the following section creates a summary of totals by category
category_totals = {}

#Loops through all the transactions entered and add up amounts by category 
for amount, category in transactions:
    #Adds the amount to the correct category total
    category_totals[category] = category_totals.get(category, 0) + amount

#Prints the category summary 
print("\nCategory Summary")
print("----------------")
for category, total in category_totals.items():
    print(f"{category}: ${total}")

    