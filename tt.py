# import time
#
# import requests
#
#
# def get_trader_info():
#     for _ in range(4):  # اجرا شدن 4 بار متوالی
#         print("#############################  Trader #######################################")
#         url = "https://api-staging.tabdealbot.com/trader/"
#
#         headers = {
#             'Authorization': 'HHRAA eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiaWQiOiJjNjQ3ZDFkOGE5ZDJkMDdkNGVkNGQ3MWM0YzhhMGUyYzFlNmUwMGVmOWFkM2E3ODYwYjNiMDI2MTkxZGQ1ZDNmIiwidXNlcl9pZCI6MjA2NiwidXNlcm5hbWUiOiI5MjE2ODU0Nzg0Iiwib3JpZ19pYXQiOjE3NDE1OTAyMDAsImRldmljZV9pZCI6ImZyb21fYXBpIiwiZXhwIjoxNzQ0MTgyMjAwfQ.vShoQhvEQohXxKpBkLXYhrAuVUR-wCSoLO7J2oMoBpUPb6cm-DBKOhzNYtELq88ZWbs_v7i4oR2fP4Un6WVRcg',
#             'Cookie': 'TS01933b4f=0150a3e24e9202bf833ca0b28b146191c5e317ae476205812a320357332b9bfa8748963e7125bf8fed53d2e702edeaf3db7f74233e'
#         }
#
#         response = requests.get(url, headers=headers)
#
#         if response.status_code == 200:
#             data = response.json()
#
#             # استخراج اطلاعات موردنظر
#             verifications = data.get("verifications", [])
#
#             for item in verifications:
#                 if item["step_display"] in ["Personal", "BankAccount", "Contact"]:
#                     print(f"عنوان: {item['step_display']}")
#                     print(f"وضعیت: {item['state_display']}")
#                     print(f"آخرین بروزرسانی: {item['updated']}")
#                     print(f"پایه‌ای بودن: {'بله' if item['is_base'] else 'خیر'}")
#                     print("-" * 40)
#         else:
#             print("خطا در دریافت اطلاعات:", response.status_code)
#
#         time.sleep(10)  # توقف 10 ثانیه‌ای بین اجراها
#
# get_trader_info()

import time
import requests


def get_trader_info():
    attempt_counter = 1  # شمارش تعداد تلاش‌ها

    for _ in range(4):  # اجرا شدن 4 بار متوالی
        print("#############################  Trader #######################################")
        print("\n")
        # اضافه کردن کامنت برای تلاش‌ها
        print(f"تلاش برای دیدن وضعیت فیلدهای مورد نظر در بار {attempt_counter}")
        print("\n")
        attempt_counter += 1  # افزایش شمارنده تلاش

        url = "https://api-staging.tabdealbot.com/trader/"

        headers = {
            'Authorization': 'HHRAA eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiaWQiOiJjNjQ3ZDFkOGE5ZDJkMDdkNGVkNGQ3MWM0YzhhMGUyYzFlNmUwMGVmOWFkM2E3ODYwYjNiMDI2MTkxZGQ1ZDNmIiwidXNlcl9pZCI6MjA2NiwidXNlcm5hbWUiOiI5MjE2ODU0Nzg0Iiwib3JpZ19pYXQiOjE3NDE1OTAyMDAsImRldmljZV9pZCI6ImZyb21fYXBpIiwiZXhwIjoxNzQ0MTgyMjAwfQ.vShoQhvEQohXxKpBkLXYhrAuVUR-wCSoLO7J2oMoBpUPb6cm-DBKOhzNYtELq88ZWbs_v7i4oR2fP4Un6WVRcg',
            'Cookie': 'TS01933b4f=0150a3e24e9202bf833ca0b28b146191c5e317ae476205812a320357332b9bfa8748963e7125bf8fed53d2e702edeaf3db7f74233e'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            # استخراج اطلاعات موردنظر
            verifications = data.get("verifications", [])

            for item in verifications:
                if item["step_display"] in ["Personal", "BankAccount", "Contact"]:
                    print(f"عنوان: {item['step_display']}")
                    print(f"وضعیت: {item['state_display']}")
                    print(f"آخرین بروزرسانی: {item['updated']}")
                    print(f"پایه‌ای بودن: {'بله' if item['is_base'] else 'خیر'}")
                    print("-" * 40)
        else:
            print("خطا در دریافت اطلاعات:", response.status_code)

        time.sleep(10)  # توقف 10 ثانیه‌ای بین اجراها


get_trader_info()
