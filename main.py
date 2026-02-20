#Purpose: To help the user manage their money by tracking income and expenses
transactions=[]  #This list stores every transaction as [amount, category]

#Student-developed procedure:
#This procedure takes an amount and a category and adds them to the transactions list.
#It then prints whether the user entered income or an expense.

def add_transaction(amount, category):
    transactions.append([amount, category])

    if amount < 0:
        print("Expenses added.")
    else:
        print("Income added.")
# Intro messages to guide the user through the procedure
print("Mini Manager")
print("=============")
print("Welcome to Mini Manager!")
print("Where you can easily track your income and expenses!")
print("Type 'stop' to stop entering your income and expenses.\n")

#Main loop that keeps asking users for transactions while they type "stop" to end it.
while True:   
    user_input = input("Enter amount (positive for income, negative for expenses) : ")
    if user_input.lower()=="stop": #Condition to exit loop
        break
    try:        #Validates that the input is a number                              s 
        amount = float(user_input)
    except:
        print("Not a number. Please try again.")
        continue   #Sends the user back to the beginning of the loop
        
    #Asks the user what the money was for
    category= input("Where did this money come from? or What was this money for?: ")
    add_transaction(amount, category)

    # Calculates the running total balance
    total = 0
    for t in transactions:    #Iteration that loops through the list
        total +=t[0]

    #Shows the user the updated balance and the category the just entered 
    print("Current balance: $", total, "(Category:", category + ")")
    print("--------------------------")

#After the user is done, the following section creates a summary of totals by category
category_totals = {}
for amount, category in transactions:
    #Adds the amount to the correct category total
    category_totals[category] = category_totals.get(category, 0)
+ amount

#Prints the category summary for the user
print("\nCategory Summary")
print("----------------")
for category, total in category_totals.items():
    print(f"{category}: ${total}")