import os
from cryptography.fernet import Fernet
import getpass

# --- ၁။ လုံခြုံရေးအတွက် Master Password သတ်မှတ်ခြင်း ---
MASTER_PASSWORD = "mysecret123"
FILE_NAME = "passwords.txt"
KEY_FILE = "key.key"

# --- ၂။ စာဝှက်ရန် သော့ (Key) ကို စီမံခြင်း ---
def load_key():
    # သော့ဖိုင် မရှိရင် အသစ်တစ်ခု ဆောက်မယ်
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    return open(KEY_FILE, "rb").read()

key = load_key()
fer = Fernet(key)

# --- ၃။ Login စနစ် ---
def login():
    attempt = getpass.getpass("Master Password ကို ရိုက်ထည့်ပါ: ")
    if attempt == MASTER_PASSWORD:
        print("✅ ဝင်ရောက်ခွင့် ပြုလိုက်ပါပြီ။")
        return True
    else:
        print("❌ Password မှားယွင်းနေပါသည်။")
        return False

# --- ၄။ Password အသစ်သိမ်းခြင်း (Encryption ပါဝင်သည်) ---
def save_password():
    site = input("Website/App အမည်: ")
    user = input("Username/Email: ")
    pwd = input("Password: ")
    
    # စာဝှက်ခြင်း (Encrypting)
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    
    with open(FILE_NAME, "a") as f:
        f.write(f"{site} | {user} | {encrypted_pwd}\n")
    print(f"🔒 '{site}' အတွက် Password ကို စာဝှက်ပြီး သိမ်းဆည်းလိုက်ပါပြီ။")

# --- ၅။ သိမ်းထားသော Password များ ကြည့်ခြင်း (Decryption ပါဝင်သည်) ---
def view_passwords():
    if not os.path.exists(FILE_NAME):
        print("⚠️ မှတ်တမ်း မရှိသေးပါ။")
        return

    print("\n--- သင့်၏ Password များ (Decrypted) ---")
    with open(FILE_NAME, "r") as f:
        for line in f:
            data = line.strip().split(" | ")
            if len(data) == 3:
                s, u, p = data
                # စာဝှက်ထားတာကို ပြန်ဖြည်ခြင်း (Decrypting)
                decrypted_pwd = fer.decrypt(p.encode()).decode()
                print(f"🌐 Site: {s} | 👤 User: {u} | 🔑 Pass: {decrypted_pwd}")

# --- ၆။ ပင်မ Program ---
if login():
    while True:
        print("\n--- Password Manager Menu ---")
        print("1. Add Password")
        print("2. View All Passwords")
        print("3. Exit")
        
        choice = input("ရွေးချယ်ပါ (1/2/3): ")

        if choice == "1":
            save_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print("👋 နှုတ်ဆက်လိုက်ပါတယ်။")
            break
        else:
            print("❗ နံပါတ် ၁၊ ၂ သို့မဟုတ် ၃ ကိုသာ ရွေးချယ်ပါ။")
