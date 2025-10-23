# bank_account.py

def main():
    initial_balance = float(input("Enter initial balance: ₹"))
    deposit_amount = float(input("Enter deposit amount: ₹"))
    
    new_balance = initial_balance + deposit_amount
    
    print(f"Initial Balance: ₹{initial_balance}")
    print(f"Deposit: ₹{deposit_amount}")
    print(f"New Balance after deposit: ₹{new_balance}")

if __name__ == "__main__":
    main()
