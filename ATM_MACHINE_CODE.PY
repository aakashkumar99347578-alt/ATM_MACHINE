blance = 1000
def check_balance(): #this funtion check the balance in account 
    global blance
    print("YOUR BALANCE IS:",blance)
def deposite(amount): #this function work on add to money in account 
    global blance 
    print("YOUR BALANCE BEFORE DEPOSITING IS ", blance)
    blance+=amount
    print("NOW YOUR BALANCE AFTER DEPOSITING IS ", blance)
def withdrawal(amount): # this function work on withdrwal to money in account 
    global blance
    print("YOUR BALANCE BEFORE WITHDRAWAL IS ", blance)
    if blance>=amount:
        blance-=amount
        print("NOW YOUR BALANCE AFTER WITHDRAWAL IS ", blance)
    else:
        print("INSUFFICIENT BALANCE")
while True:
    #this is the menu of your account 
    print("-------------WELCOME TO ATM MACHINE----")
    print("-------------ATM MACHINE MENU-------------")
    print("1.check balance")
    print("2.deposite")
    print("3.withdrawal")
    print("4.exit")
    choice = int(input("ENTER YOUR CHOICE FROM THE ATM MACHINE MENU:"))
    if choice == 1:
        check_balance()
    elif choice == 2:
        amount = int(input("enter the amount to deposite:"))
        deposite(amount)
        print("SUCCESSFULLY DEPOSITED TO YOUR BANK ACCOUNT")
    elif choice == 3:
        amount = int(input("enter the amount to withdrawal:"))
        withdrawal(amount)
        print("SUCCESSFULLY WITHDRAWN FROM YOUR BANK ACCOUNT")
    elif choice == 4:
        print("THANKS FOR USING OUR ATM MACHINE SERVICE")
        print("HAVE A NICE DAY AHEAD")
        print("VISIT AGAIN SOON")
        break
    else:
        print("INVALID CHOICE, PLEASE TRY AGAIN1")
    
