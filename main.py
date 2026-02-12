#Purpose: To help the user manage their money
transactions[]

def add_transactions(amount, category):
    transactions.append([amount, category])

    if amount < 0:
        print("Expenses saved.")
    else:
        print("Income saved.")

total = 0
for x in transactions:
    total +=x[0]

print(f"Current balence: $",total)
print("--------------------------")

def is_number(text):
    allowed = "0123456789.-"
    for ch in text:
        if ch not allowed:
            return False
        if text.count("-")> 1 or text.count(".") > 1:
            return False
        if "-" in text and text.index("-") !=0:
            return False
        return True

print("Mini Manager")
print("=============")
print("Welcome to Mini Manager!")
print("Where you'll be able to easily track your income and expenses!")
print("Type 'quit' to exit.\n")


while True:
    user_input = input("Enter amount (positive for income, negative for expenses) : ")
    if user_input.lower()=="quit":
        print("Exit program. Bye!")
        break

