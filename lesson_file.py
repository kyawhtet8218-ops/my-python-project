file_name = "my_data.txt"

# ၁။ File ထဲသို့ စာသားများ ရေးသားခြင်း (Writing)
# 'w' ဆိုတာ write ကို ပြောတာပါ (ဖိုင်အသစ်ဆောက်မယ်၊ ရှိပြီးသားဆိုရင် အပေါ်က ထပ်ရေးမယ်)
with open(file_name, "w") as file:
    file.write("ဒါကတော့ ပထမဆုံး သိမ်းလိုက်တဲ့ စာသားပါ။\n")
    file.write("Python နဲ့ ဖိုင်သိမ်းရတာ တကယ်လွယ်ပါတယ်။\n")
    print("ဖိုင်ထဲသို့ အောင်မြင်စွာ သိမ်းဆည်းပြီးပါပြီ။")

print("-" * 20)

# ၂။ File ထဲက အချက်အလက်များကို ပြန်ဖတ်ခြင်း (Reading)
# 'r' ဆိုတာ read ကို ပြောတာပါ
print("ဖိုင်ထဲကစာတွေကို ပြန်ဖတ်ပြပါမယ် -")
try:
    with open(file_name, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("ဖိုင်ကို ရှာမတွေ့ပါ။")

# ၃။ ရှိပြီးသားဖိုင်ထဲကို စာသားအသစ် ထပ်တိုးခြင်း (Appending)
# 'a' ဆိုတာ append (အောက်ကနေ ထပ်တိုးမယ်) လို့ ဆိုလိုတာပါ
with open(file_name, "a") as file:
    file.write("ဒီစာသားကတော့ နောက်မှ ထပ်တိုးလိုက်တာပါ။\n")
