import os

FILE_NAME = "library_data.txt"
library = {}

# ၁။ ဖိုင်ထဲက Data တွေကို Program စတာနဲ့ ပြန်ဖတ်မယ့် Function
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                # စာကြောင်းကို Title နဲ့ Author ပြန်ခွဲထုတ်ခြင်း
                title, author = line.strip().split("|")
                library[title] = author

# ၂။ Data တွေကို ဖိုင်ထဲ သိမ်းမယ့် Function
def save_data():
    with open(FILE_NAME, "w") as file:
        for title, author in library.items():
            file.write(f"{title}|{author}\n")

def add_book():
    title = input("စာအုပ်အမည်: ")
    author = input("စာရေးဆရာ: ")
    library[title] = author
    save_data() # ထည့်ပြီးတိုင်း ဖိုင်ထဲ သိမ်းမယ်
    print("သိမ်းဆည်းပြီးပါပြီ။")

def show_books():
    load_data() # ဖိုင်ထဲက data ကို အရင်ဖတ်မယ်
    if not library:
        print("\nစာအုပ်စာရင်း မရှိသေးပါ။")
    else:
        print("\n--- စာအုပ်စာရင်း ---")
        for t, a in library.items():
            print(f"Title: {t} | Author: {a}")

def delete_book():
    title = input("ဖျက်လိုသော စာအုပ်အမည်ကို ရိုက်ပါ: ")
    if title in library:
        del library[title]
        save_data() # ဖိုင်ထဲမှာပါ ပျက်သွားအောင် ပြန်သိမ်းမယ်
        print(f"'{title}' ကို ဖျက်ပြီးပါပြီ။")
    else:
        print("ရှာမတွေ့ပါ။")

# --- Main Program ---
load_data() # Program စတာနဲ့ အရင်က ရှိပြီးသားစာရင်းကို ဆွဲတင်မယ်

while True:
        print("\n1. Add | 2. View | 3. Delete | 4. Exit") # 3. Delete ထည့်လိုက်တယ်
    choice = input("ရွေးချယ်ပါ: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        show_books()
    elif choice == '3':
        delete_book() # Delete function ကို ခေါ်လိုက်တယ်
    elif choice == '4':
        break

