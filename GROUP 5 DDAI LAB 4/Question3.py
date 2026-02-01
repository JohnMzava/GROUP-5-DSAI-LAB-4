def transaction_counter():
    amount = float(input("Enter transaction amount (0 to stop): "))

    if amount == 0:
        return 0  
    else:
        return 1 + transaction_counter()  


total_transactions = transaction_counter()
print(f"Total number of transactions entered: {total_transactions}")
