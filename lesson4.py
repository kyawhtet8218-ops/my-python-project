# User ဆီက အမှတ်ကို တောင်းယူပါမယ်
score = int(input("သင့်ရဲ့ စာမေးပွဲအမှတ်ကို ရိုက်ထည့်ပါ (0-100): "))

# Grade စစ်ဆေးခြင်း Logic
if score >= 80:
    grade = "A"
    message = "ထူးချွန်ပါတယ်။ ဂုဏ်ယူပါတယ်!"
elif score >= 65:
    grade = "B"
    message = "ကောင်းမွန်ပါတယ်။"
elif score >= 50:
    grade = "C"
    message = "သင့်တင့်ပါတယ်။"
elif score >= 40:
    grade = "D"
    message = "ကြိုးစားဖို့ လိုပါသေးတယ်။"
else:
    grade = "Fail"
    message = "စိတ်မကောင်းပါဘူး။ ကျရှုံးခဲ့ပါတယ်။"

# ရလဒ်ကို ထုတ်ပြခြင်း
print("-" * 25)
print("ရရှိတဲ့ Grade ကတော့: " + grade)
print("မှတ်ချက်: " + message)
print("-" * 25)

