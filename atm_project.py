# အစပိုင်းမှာ လက်ကျန်ငွေကို 0 လို့ သတ်မှတ်ထားပါမယ်
balance = 0

def check_balance():
    print(f"\nလက်ရှိ လက်ကျန်ငွေ: {balance} ကျပ်")

def deposit(amount):
    global balance
    balance += amount
    print(f"\n{amount} ကျပ် ထည့်သွင်းမှု အောင်မြင်ပါသည်။")

def withdraw(amount):
    global balance
    if amount > balance:
        print("\nစိတ်မကောင်းပါဘူး၊ လက်ကျန်ငွေ မလုံလောက်ပါ။")
    else:
        balance -= amount
        print(f"\n{amount} ကျပ် ထုတ်ယူမှု အောင်မြင်ပါသည်။")

# --- Main Program Loop ---
while True:
    print("\n--- ATM စနစ် ---")
    print("1. လက်ကျန်ငွေစစ်မယ်")
    print("2. ငွေထည့်မယ်")
    print("3. ငွေထုတ်မယ်")
    print("4. ထွက်မယ်")
    
    choice = input("\nဘာလုပ်ချင်လဲ ရွေးချယ်ပါ (1/2/3/4): ")

    if choice == '1':
        check_balance()
    elif choice == '2':
        amt = int(input("ထည့်မည့် ငွေပမာဏကို ရိုက်ထည့်ပါ: "))
        deposit(amt)
    elif choice == '3':
        amt = int(input("ထုတ်မည့် ငွေပမာဏကို ရိုက်ထည့်ပါ: "))
        withdraw(amt)
    elif choice == '4':
        print("အသုံးပြမှုအတွက် ကျေးဇူးတင်ပါသည်။")
        break
    else:
        print("မှားယွင်းနေပါသည်။ ပြန်လည်ရွေးချယ်ပါ။")
