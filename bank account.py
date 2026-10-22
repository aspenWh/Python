def withdraw(amount, balance):
    if amount > balance:
        raise Exception("Insufficient funds")
    
    return balance - amount


#in other system
# from bank_accouont import withdraw
# balance = 100
# try:
#      Amount = int(input("Enter amount to withdraw: "))
#      balance = withdraw(amount, balance)
#except:
#    print("An error occurred during withdrawal.")