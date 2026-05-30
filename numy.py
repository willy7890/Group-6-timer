import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('atm_system.db')
    cursor = conn.cursor()
    # Create Accounts and Transactions tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS accounts 
                      (acc_no TEXT PRIMARY KEY, pin TEXT, balance REAL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions 
                      (id INTEGER PRIMARY KEY, acc_no TEXT, type TEXT, amount REAL, timestamp TEXT)''')
    
    # Create a test account (Acc: 12345, PIN: 0000, Balance: 500)
    try:
        cursor.execute("INSERT INTO accounts VALUES ('12345', '0000', 500.0)")
        conn.commit()
    except sqlite3.IntegrityError:
        pass 
    conn.close()

def log_transaction(acc_no, trans_type, amount):
    conn = sqlite3.connect('atm_system.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (acc_no, type, amount, timestamp) VALUES (?, ?, ?, ?)",
                   (acc_no, trans_type, amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def atm_session(acc_no):
    while True:
        print("\n--- ATM MENU ---")
        print("1. Balance  2. Deposit  3. Withdraw  4. History  5. Exit")
        choice = input("Select: ")

        conn = sqlite3.connect('atm_system.db')
        cursor = conn.cursor()

        if choice == '1':
            cursor.execute("SELECT balance FROM accounts WHERE acc_no=?", (acc_no,))
            print(f"Current Balance: ${cursor.fetchone()[0]:.2f}")
        
        elif choice == '2':
            amt = float(input("Amount to Deposit: "))
            cursor.execute("UPDATE accounts SET balance = balance + ? WHERE acc_no=?", (amt, acc_no))
            conn.commit()
            log_transaction(acc_no, "DEPOSIT", amt)
            print("Done!")

        elif choice == '3':
            amt = float(input("Amount to Withdraw: "))
            cursor.execute("SELECT balance FROM accounts WHERE acc_no=?", (acc_no,))
            bal = cursor.fetchone()[0]
            if amt <= bal:
                cursor.execute("UPDATE accounts SET balance = balance - ? WHERE acc_no=?", (amt, acc_no))
                conn.commit()
                log_transaction(acc_no, "WITHDRAW", amt)
                print("Cash dispensed.")
            else:
                print("Insufficient funds.")

        elif choice == '4':
            cursor.execute("SELECT type, amount, timestamp FROM transactions WHERE acc_no=?", (acc_no,))
            for t in cursor.fetchall():
                print(f"{t[2]} | {t[0]}: ${t[1]}")

        elif choice == '5':
            break
        conn.close()

if __name__ == "__main__":
    init_db()
    acc = input("Account Number: ")
    pin = input("PIN: ")
    
    conn = sqlite3.connect('atm_system.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE acc_no=? AND pin=?", (acc, pin))
    if cursor.fetchone():
        atm_session(acc)
    else:
        print("Login Failed.")
    conn.close()
