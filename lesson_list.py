# ၁။ List တစ်ခု တည်ဆောက်ခြင်း (Square brackets [] ကို သုံးပါတယ်)
fruits = ["Apple", "Banana", "Orange", "Mango"]

# ၂။ List ထဲက အချက်အလက်ကို ထုတ်ယူခြင်း (Index လို့ ခေါ်ပါတယ်)
# Coding မှာ ရေတွက်ပုံက 0 ကနေ စပါတယ်
print("ပထမဆုံး အသီး: " + fruits[0]) # Apple ကို ထွက်ပါမယ်
print("ဒုတိယ အသီး: " + fruits[1]) # Banana ကို ထွက်ပါမယ်

# ၃။ List ထဲကို အသီးအသစ် ထပ်ထည့်ခြင်း
fruits.append("Strawberry")

# ၄။ List တစ်ခုလုံးကို Loop ပတ်ပြီး ထုတ်ပြခြင်း
print("\nကျွန်တော့်ဆီမှာ ရှိတဲ့ အသီးများ -")
for fruit in fruits:
    print("- " + fruit)

# ၅။ List ထဲမှာ အသီး ဘယ်နှစ်လုံး ရှိလဲ စစ်ခြင်း
print("\nစုစုပေါင်း အသီးအရေအတွက်: " + str(len(fruits)))
