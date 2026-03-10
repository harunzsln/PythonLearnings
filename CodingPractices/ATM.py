haveMoney = 2000

choose = input("Type 'i' to insert card into the ATM, or 'q' to quit: ")
if choose == "i":
    while True:
        action = input(
            """
 1- Withdraw Money
 2- Deposit Money
 3- Account information
 4- Exit                  
                   Choose an action (1, 2, 3, 4): """
        )

        if action == "1":
            withdraw_amount = float(input("Enter amount to withdraw: "))
            if withdraw_amount > haveMoney:
                print("Insufficient funds. Your balance is: {}".format(haveMoney))
            else:
                haveMoney -= withdraw_amount
                print("Withdrawal successful. New balance is: {}".format(haveMoney))
        if action == "2":
            deposit_amount = float(input("Enter amount to deposit: "))
            haveMoney += deposit_amount
            print("Deposit successful. New balance is: {}".format(haveMoney))
        if action == "3":
            print("Account İnformation\nAccount Owner: Harun Özaslan\nAccount IBAN: TR80 XXXX XXXX XXXX XXXXX\nAccount Balance: {}".format(haveMoney))
        if action == "4":
            print("Get your card back from ATM. Exiting the ATM. Goodbye!")
            break
else:
    print("Exiting the ATM. Goodbye!")
