accounts = {}

count = int(input("How many accounts do you want to create? "))

for i in range(1, count + 1):
    print(f"\nCreating account {i}")
    owner = input("Account owner name: ")
    initial = float(input("Initial balance: "))
    accounts[owner] = initial

while True:
    print("Welcome to the bank!")
    print("\nSelect an option:")
    print("1. Show balances")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Above-average accounts")
    print("5. Exit")

    option = input("Enter option: ")

    if option == "1":
        if not accounts:
            print("No accounts found.")
        else:
            for owner, bal in accounts.items():
                print(owner, "→", bal)

    elif option == "2":
        owner = input("Account name: ")
        if owner in accounts:
            amt = float(input("Amount: "))
            accounts[owner] += amt
            print("Deposit successful.")
        else:
            print("Account not found.")

    elif option == "3":
        owner = input("Account name: ")
        if owner in accounts:
            amt = float(input("Amount: "))
            if accounts[owner] >= amt:
                accounts[owner] -= amt
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    elif option == "4":
        if accounts:
            avg = sum(accounts.values()) / len(accounts)
            print("Average balance:", avg)
            for owner, bal in accounts.items():
                if bal > avg:
                    print(owner, "→", bal)
        else:
            print("No accounts available.")

    elif option == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid option.")