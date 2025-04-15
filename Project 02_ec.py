import json
import re

address_book = {}
file_name = "addressbook.json"

def display_menu():
    print("Menu")
    print("-------------------------------")
    print("1. Look up email address")
    print("2. Add new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Print Address book")
    print("6. Quit the program")
    print()
def look_up_email():
    n = input("Enter a name: ")
    if not n:
        print("Name can't be empty.")
        return
    email = input("Enter email address: ")
##    if not re.match(r"[^@] + @[^@]+\.[^@]+", email):
##        print("Invalid email format.")
##        return
##    
    if name in address_book:
        print("Name: ", n)
        print(f"Email: {address_book[n]}")
    else:
        print("The specified name was not found")

def add_name_and_email():
    name = input("Enter name: ")
    email = input("Enter email address: ")
    if name in address_book:
        print("The name already exists")
    else:
        address_book[name] = email
        print("Name and address have been added")

def change_emailadress():
    name = input("Enter name: ")
    if name in address_book:
        new = input("Enter the new address: ")
        address_book[n] = new_email
        print("Information updated")
    else:
        print("Name not found in the address book")
        
def print_list_of_emails():
    sorted_address_book = sorted(address_book.items())
    for name, email in sorted_address_book:
        print(f"{name}: {email}")

def delete_name_and_email():
    name = input("Enter name: ")
    if name in address_book:
        del address_book[name]
        print("Information deleted")
    else:
        print("The specified name was not found")

def sorted_address_book_print():
    print("Address Book:")
    sorted_address_book = sorted(address_book.items())
    for name, email in sorted_address_book:
        
        print(f"{name} {email}")

def load_data_from_file():
    global address_book
    try:
        with open(file_name, "r") as file:
            address_book = json.load(file)
    except FileNotFoundError:
        print("File not found. Starting with empty address book")

def save_data_to_file():
    with open(file_name, "w") as file:
        json.dump(address_book, file)
    print("Information saved")

def main():
    load_data_from_file()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Invalid choice. Enter a number from 1 to 6.")
            continue 
        if choice == "1":
            look_up_email()
            print("\n")
        elif choice == "2":
            add_name_and_email()
            print("\n")
        elif choice == "3":
            cha_email()
            print("\n")
        elif choice == "4":
            delete_email()
            print("\n")
        elif choice == "5":
            print()
            print_sorted_address_book()
            print("\n")
        elif choice == "6":
            save_data_to_file()
            break
        else:
            print("Invalid choice. Please try again")
main()
