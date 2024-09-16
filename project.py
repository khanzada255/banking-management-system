#Banking Management System


balance = 5000  # Consistently use 'balance' with lowercase
pin = 1234
choice = 0

while choice != 5:
    print("\nPress 1 to deposit the amount.")
    print("Press 2 to withdraw the amount.")
    print("Press 3 to check the current balance.")
    print("Press 4 to change the pin.")
    print("Press 5 to Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        # Deposit amount
        amount = int(input("Enter the amount you want to deposit: "))
        balance += amount
        print(f"Your amount has been deposited successfully. Current balance: {balance}")

    elif choice == 2:
        # Withdraw amount
        checkpoint = int(input("Enter your pin: "))
        if checkpoint == pin:
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"You have successfully withdrawn {amount}. Current balance: {balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Wrong pin!")

    elif choice == 3:
        # Check balance
        checkpoint = int(input("Enter your pin: "))
        if checkpoint == pin:
            print(f"Your current balance is: {balance}")
        else:
            print("Wrong pin!")

    elif choice == 4:
        # Change pin
        checkpoint = int(input("Enter your current pin: "))
        if checkpoint == pin:
            new_pin = int(input("Enter your new pin: "))
            pin = new_pin
            print("Your pin has been updated successfully.")
        else:
            print("Wrong pin!")

    elif choice == 5:
        print("Exiting... Thanks for using our service!")
    else:
        print("Invalid choice! Please select a valid option.")
