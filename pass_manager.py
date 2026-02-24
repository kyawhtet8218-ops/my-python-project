import os
import getpass

MASTER_PASSWORD = "mysecret123"
FILE_NAME = "passwords.txt"

def login():
    attempt = getpass.getpass("Master Password ကို ရိုက်ထည့်ပါ: ")
    if attempt == MASTER_PASSWORD:
        print("ဝင်ရောက်ခွင့် ပြုလိုက်ပါပြီ။")
        return True
    else:
        print("Password မှားယွင်းနေပါသည်။")
        return False

def save_password():
    site = input("Website/App အမည်: ")
    user = input("Username/Email: ")
    pwd = input("Password: ")
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
# ပထမဆုံး Login ဝင်ခိုင်းမယ်
if login():
    while True:
        print("\n1. Add Password | 2. View All | 3. Exit")
        choice = input("ရွေးချယ်ပါ: ")

        if choice == "1":
            save_password()  # ဒီနေရာမှာ function ကို ပြန်ခေါ်ပေးရပါတယ်
        elif choice == "2":
            view_passwords() # ဒီနေရာမှာလည်း function ကို ခေါ်ရပါမယ်
        elif choice == "3":
            print("Bye Bye!")
            break            # 3 နှိပ်ရင် program ရပ်သွားပါမယ်
        else:
            print("နံပါတ် ၁၊ ၂ သို့မဟုတ် ၃ ကိုသာ ရွေးချယ်ပါ။")

