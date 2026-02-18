#Purpose: To help the user manage their money
transactions=[]

def add_transaction(amount, category):
    transactions.append([amount, category])

    if amount < 0:
        print("Expenses added.")
    else:
        print("Income added.")

print("Mini Manager")
print("=============")
print("Welcome to Mini Manager!")
print("Where you'll be able to easily track your income and expenses!")
print("Type 'stop' to stop entering your income and expenses.\n")

while True:   
    user_input = input("Enter amount (positive for income, negative for expenses) : ")
    if user_input.lower()=="stop":
        break
    try:                                      #https://www.youtube.com/watch?v=n8NfyU5pX2U&t=249s 
        amount = float(user_input)
    except:
        print("Not a number. Please try again.")
        continue

    category= input("What is this/was money for?: ")
    add_transaction(amount, category)

    total = 0
    for t in transactions:
        total +=t[0]

    print("Current balance: $", total, "(Category:", category + ")")
    print("--------------------------")

category_totals = {}
for amount, category in transactions:
    category_totals[category] = category_totals.get(category, 0)
+ amount

print("\nCategory Summary")
print("----------------")
for category, total in category_totals.items():
    print(f"{category}: ${total}")