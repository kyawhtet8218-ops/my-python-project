import os

FILE_NAME = "passwords.txt"

def save_password():
    site = input("Website/App အမည်: ")
    user = input("Username/Email: ")
    pwd = input("Password: ")
    
    # ဖိုင်ထဲမှာ ပုံစံတကျ သိမ်းမယ် (Site | User | Password)
    with open(FILE_NAME, "a") as f:
        f.write(f"{site} | {user} | {pwd}\n")
    print("သိမ်းဆည်းပြီးပါပြီ။")

def view_passwords():
    if not os.path.exists(FILE_NAME):
        print("မှတ်တမ်း မရှိသေးပါ။")
        return

    print("\n--- သင့်၏ Password များ ---")
    with open(FILE_NAME, "r") as f:
        for line in f:
            data = line.strip().split(" | ")
            if len(data) == 3:
                s, u, p = data
                print(f"Site: {s} | User: {u} | Pass: {p}")

# --- Main Program ---
while True:
    print("\n1. Add Password | 2. View All | 3. Exit")
    choice = input("ရွေးချယ်ပါ: ")

    if choice == "1":
        save_password()
    elif choice == "2":
        view_passwords()
    elif choice == "3":
        break

