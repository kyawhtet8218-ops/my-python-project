# ၁။ Dictionary တစ်ခု တည်ဆောက်ခြင်း (Curly brackets {} ကို သုံးပါတယ်)
phonebook = {
    "Aung Aung": "09-111111",
    "Su Su": "09-222222",
    "Kyaw Kyaw": "09-333333"
}

# ၂။ အချက်အလက်ကို Key သုံးပြီး ထုတ်ယူခြင်း
print("Su Su ရဲ့ ဖုန်းနံပါတ်: " + phonebook["Su Su"])

# ၃။ အချက်အလက်အသစ် ထပ်ထည့်ခြင်း
phonebook["Mya Mya"] = "09-444444"

# ၄။ ရှိပြီးသား နံပါတ်ကို ပြင်ဆင်ခြင်း
phonebook["Aung Aung"] = "09-999999"

# ၅။ ဖုန်းစာအုပ်ထဲက အားလုံးကို ထုတ်ပြခြင်း
print("\n--- ကျွန်တော့်ရဲ့ ဖုန်းစာအုပ် ---")
for name, number in phonebook.items():
    print(f"အမည်: {name} | ဖုန်း: {number}")

# ၆။ နာမည်တစ်ခု ရှိမရှိ စစ်ဆေးခြင်း
search_name = "Su Su"
if search_name in phonebook:
    print(f"\n{search_name} သည် ဖုန်းစာအုပ်ထဲမှာ ရှိပါသည်။")
