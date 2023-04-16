# Imported Software
import json
import random
import string
import time
import os

def banner():
    owl_art = """
      Welcome to OwlLock
 ___________________________
|      __                   |
|     [  ]                  |
|    ,----..                |
|   /   /   \               |
|  |   :  |  |              |
|  |   | : : |   ,---.      |
|  ;   | | | | /___/| :;    | 
|  |   | : : |  \   ;/ ||   | 
|  ;   |  |  |   \ \  \ .;  | 
|   \   \   /     ` \  \    |
|    `----'         `----'  |
 \_________________________/
"""
    # Split the owl art into separate lines
    owl_lines = owl_art.split("\n")

    # Print each line with a delay of 0.2 seconds between each line
    for line in owl_lines:
        print(line)
        time.sleep(0.2)

def generate_password(length):

    # Generates a random password with a given length.
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''
    while True:
        password = ''.join(random.choice(chars) for _ in range(length))

        if any(c.islower() for c in password) and \
            any(c.isupper() for c in password) and \
            any(c.isdigit() for c in password) and \
            any(c in string.punctuation for c in password):
            break
        
    return password

def load_passwords(file_name):
    # Loads account passwords from a JSON file.
    try:
        # Attempts to load the password file.
        with open(file_name, 'r') as f:
            # Checks if the file exists.
            if os.path.getsize(file_name) > 0:
                return json.load(f)
            else:
                return {}
    # Will display an error message if file not found.
    except FileNotFoundError:
        raise Exception("File not found. Please create a passwords.json file.")


def save_passwords(passwords, file_name):
    
    # Saves account passwords to a JSON file.
    with open(file_name, 'w') as f:
        # Writes passwords to JSON file.
        json.dump(passwords, f)
        f.write("\n")

# Adds a new account to the password manager.

def add_account(passwords):

    # Error checking for no input in variable
    while True:
        account_name = input("Enter account name: ")
        # Error checking for no input in variable
        if account_name == "":
            print("Please enter a valid account name")
        else: 
            break
    account_password = input("Enter account password (leave blank to generate one): ")

    # Will generate password if no input provided
    if not account_password:
        account_password = generate_password(12)
        print("Generated password:", account_password)
        
    passwords[account_name] = account_password
    print("Account added successfully.")

# Deletes one or multiple existing accounts from the password manager.
def delete_account(passwords):

    account_names = input("Enter account name(s) to delete (separated by commas): ").split(",")
    deleted_accounts = []

    # Check if the account exists
    for account_name in account_names:
        if account_name.strip() in passwords:
            del passwords[account_name.strip()]
            deleted_accounts.append(account_name.strip())

    if deleted_accounts:
        print(f"Account(s) {', '.join(deleted_accounts)} deleted successfully.")
    else:
        print("Account(s) not found.")

# Generates new passwords for all existing accounts in the password manager.
def generate_passwords(passwords):

    print("\nGenerate new password for which account(s)?")
    account_names = list(passwords.keys())

    for i, account_name in enumerate(account_names):
        print(f"{i+1}. {account_name}")
    # Checks how many accounts
    print(f"{len(account_names)+1}. Cancel")
    choices = input("\nEnter choice(s), separated by commas: ")
    choices = choices.split(",")
    choices = [int(choice.strip()) for choice in choices if choice.strip().isdigit()]

    for choice in choices:
        if choice == len(account_names)+1:
            break

        account_name = account_names[choice-1]
        account_password = generate_password(12)
        passwords[account_name] = account_password
        print(f"New password for {account_name}: {account_password}")

    print("\nPasswords generated successfully.")


def main():
    banner()
    file_name = "passwords.json"
    try:
        passwords = load_passwords(file_name)

    except FileNotFoundError:
        passwords = {}

    while True:
        print(("\n"))
        print("0. BANNER ( ^ . ^ )")
        print("1. List accounts")
        print("2. Add account")
        print("3. Delete account")
        print("4. Generate new passwords")
        print("5. Quit")
        choice = input("\nEnter choice: ")
        
        if choice == "0":
            banner()

        elif choice == "1":
            print("\nAccounts:")
            for account_name, account_password in passwords.items():
                print(f"{account_name}: {account_password}")

        elif choice == "2":
            add_account(passwords)

        elif choice == "3":
            delete_account(passwords)

        elif choice == "4":
            generate_passwords(passwords)

        elif choice == "5":
            save_passwords(passwords, file_name)
            print("Exiting.")
            break

        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
