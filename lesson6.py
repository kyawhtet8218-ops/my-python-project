# ၁။ Function တစ်ခုကို တည်ဆောက်ခြင်း (Define)
def greet_user(name):
    """နှုတ်ဆက်စကား ပြောကြားပေးတဲ့ Function"""
    print("မင်္ဂလာပါ " + name + " ခင်ဗျာ။")
    print("Programming လေ့လာနေတာ တိုးတက်ပါစေ။")

# ၂။ အပေါင်းအနှုတ် တွက်ပေးမယ့် Function
def add_numbers(num1, num2):
    return num1 + num2

# --- Function တွေကို စတင်အသုံးပြုခြင်း (Calling) ---

# ပထမ Function ကို နာမည်ခေါ်သုံးခြင်း
greet_user("Aung Aung")
print("-" * 20)

# ဒုတိယ Function ကို သုံးပြီး ရလဒ်ယူခြင်း
result = add_numbers(50, 75)
print("အဖြေမှာ: " + str(result) + " ဖြစ်ပါတယ်။")
