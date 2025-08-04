import json
import os

filepath = "jsonfile.json"

def read_creadentials(filepath):
    try:
        with open(filepath, "r") as file:
            content = file.read()
            if not content.strip(): 
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []

def write_creadentials(filepath, data):
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)

def add_credentials(filepath, Website, Username, Password):
    data = read_creadentials(filepath)
    data.append({
        "website": Website,
        "username": Username,
        "password": Password
    })
    write_creadentials(filepath, data)

def delete_credentials(filepath, website):
    data = read_creadentials(filepath)
    new_data = [entry for entry in data if entry["website"] != website]
    write_creadentials(filepath, new_data)



def show_menu():
    print("1. Add new Credentials")
    print("2. View all saved credentials")
    print("3. Search credentials by website")
    print("4. Delete a creadential")
    print("5. Exit")


def main():
    print("Welcome to Password Locker!")
    print("----------------------------------")
    choice = 0
    while choice != 5:
        show_menu()
        choice = input("Select an option: ")
        if choice == "1":
            Website = input("Website: ")
            Username = input("Username: ")
            Password = input("Password: ")
            add_credentials(filepath, Website, Username, Password)
            print("Saved succefully!")
        elif choice == "2":
            print("--- Saved Credentials ---")
            all_creds = read_creadentials(filepath)
            for i in all_creds:
                print(f">> {i}")
        elif choice == "3":
            search = input("Enter website: ")
            read_creadentials(filepath)



        elif choice == "3":
            search = input("Enter website: ").lower()
            found = False
        for entry in read_creadentials(filepath):
            if entry["website"].lower() == search:
                print(f">> Website: {entry['website']}")
                print(f"   Username: {entry['username']}")
                print(f"   Password: {entry['password']}")
                found = True
                break
        if not found:
            print("No credentials found for that website.")







if __name__ == "__main__":
    main()