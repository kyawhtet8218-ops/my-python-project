# စာအုပ်စာရင်းကို Dictionary ထဲမှာ သိမ်းမယ် {စာအုပ်အမည်: စာရေးဆရာ}
library = {}

def add_book():
    title = input("စာအုပ်အမည် ရိုက်ထည့်ပါ: ")
    author = input("စာရေးဆရာအမည် ရိုက်ထည့်ပါ: ")
    library[title] = author
    print(f"\n'{title}' ကို စာရင်းထဲ ထည့်သွင်းပြီးပါပြီ။")

def show_books():
    if not library:
        print("\nစာကြည့်တိုက်ထဲမှာ စာအုပ်စာရင်း မရှိသေးပါ။")
    else:
        print("\n--- လက်ရှိရှိသော စာအုပ်များ ---")
        for title, author in library.items():
            print(f"စာအုပ်: {title} | စာရေးဆရာ: {author}")

def search_book():
    query = input("ရှာဖွေလိုသော စာအုပ်အမည်ကို ရိုက်ပါ: ")
    if query in library:
        print(f"\nတွေ့ရှိပါသည်! '{query}' ၏ စာရေးဆရာမှာ {library[query]} ဖြစ်ပါတယ်။")
    else:
        print("\nရှာမတွေ့ပါ။ စာအုပ်အမည် မှန်ကန်စွာ ရိုက်ထည့်ပါ။")

# --- Main Program Loop ---
while True:
    print("\n===== စာကြည့်တိုက် စီမံခန့်ခွဲမှု စနစ် =====")
    print("1. စာအုပ်အသစ်ထည့်မယ်")
    print("2. စာအုပ်စာရင်းကြည့်မယ်")
    print("3. စာအုပ်ရှာမယ်")
    print("4. ပရိုဂရမ်မှ ထွက်မယ်")
    
    try:
        choice = input("\nလုပ်ဆောင်လိုသည့် အမှတ်စဉ်ကို ရွေးပါ: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            show_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            print("အသုံးပြုသည့်အတွက် ကျေးဇူးတင်ပါသည်။ ဘိုင့်ဘိုင်!")
            break
        else:
            print("အမှားရှိပါသည်: နံပါတ် ၁ မှ ၄ အထိသာ ရွေးချယ်ပေးပါ။")
            
    except Exception as e:
        print(f"မထင်မှတ်ထားသော အမှားတစ်ခု ဖြစ်ပေါ်ခဲ့သည်: {e}")
