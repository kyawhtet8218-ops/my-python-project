# ၁။ Function ကို သတ်မှတ်ခြင်း (စက်ရုံတည်ဆောက်ခြင်း)
def multiply_two_numbers(a, b):
    result = a * b
    return result

# ၂။ Function ကို အသုံးချခြင်း (ခလုတ်နှိပ်ပြီး ခိုင်းစေခြင်း)

# ဥပမာ (၁) - ၅ နဲ့ ၁၀ နဲ့ မြှောက်ခိုင်းမယ်
answer1 = multiply_two_numbers(5, 10)
print("၅ နှင့် ၁၀ ကို မြှောက်ရင် - " + str(answer1))

# ဥပမာ (၂) - User ဆီက တောင်းပြီး မြှောက်ခိုင်းမယ်
x = int(input("ပထမဂဏန်း ရိုက်ပါ: "))
y = int(input("ဒုတိယဂဏန်း ရိုက်ပါ: "))

final_answer = multiply_two_numbers(x, y)
print("အဖြေမှာ: " + str(final_answer))
