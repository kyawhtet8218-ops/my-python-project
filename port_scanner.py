import socket

def scan_port(target, port):
    try:
        # Network ချိတ်ဆက်ဖို့ ကြိုးစားမယ်
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # ၁ စက္ကန့်ပဲ စောင့်မယ်
        
        # Target ရဲ့ Port ကို စမ်းချိတ်ကြည့်မယ်
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()
    except:
        pass

# --- Main Program ---
target_ip = input("Scan ဖတ်မည့် IP သို့မဟုတ် Domain (ဥပမာ- google.com): ")

print(f"Scanning Target: {target_ip}...")
print("-" * 30)

# Port 1 ကနေ 100 အထိ စမ်းစစ်မယ်
for port in range(1, 101):
    scan_port(target_ip, port)

print("-" * 30)
print("Scanning ပြီးဆုံးပါပြီ။")
