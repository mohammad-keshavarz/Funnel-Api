# import pandas as pd
# from datetime import datetime
#
# # داده‌های ثابت برای هر دیتاست
# data_1 = {
#     'شماره تلفن': ['09121234567'],
#     'کد ملی': ['1234567890'],
#     'تاریخ تولد': ['1990-01-15']
# }
#
# data_2 = {
#     'شماره تلفن': ['09132345678'],
#     'کد ملی': ['9876543210'],
#     'تاریخ تولد': ['1988-02-14']
# }
#
# data_3 = {
#     'شماره تلفن': ['09141234567'],
#     'کد ملی': ['6789012345'],
#     'تاریخ تولد': ['1991-04-22']
# }
#
# # ایجاد دیتاست‌ها
# df1 = pd.DataFrame(data_1)
# df2 = pd.DataFrame(data_2)
# df3 = pd.DataFrame(data_3)
#
# # تابع اعتبارسنجی شماره تلفن
# def validate_phone_number(phone):
#     if len(phone) == 11 and phone.startswith(('091', '093')) and phone.isdigit():
#         return True
#     return False
#
# # تابع اعتبارسنجی کد ملی
# def validate_national_id(national_id):
#     if len(national_id) == 10 and national_id.isdigit():
#         return True
#     return False
#
# # تابع اعتبارسنجی تاریخ تولد
# def validate_birthdate(birthdate):
#     try:
#         birthdate_obj = datetime.strptime(birthdate, '%Y-%m-%d')
#         if birthdate_obj < datetime.now() and (datetime.now() - birthdate_obj).days / 365.25 >= 18:
#             return True
#     except ValueError:
#         pass
#     return False
#
#
# # تست کیس‌های مثبت (Valid Test Cases)
# def test_valid_cases(df):
#     # شماره تلفن معتبر
#     assert validate_phone_number(df['شماره تلفن'][0]) == True
#     # کد ملی معتبر
#     assert validate_national_id(df['کد ملی'][0]) == True
#     # تاریخ تولد معتبر (سن حداقل 18 سال)
#     assert validate_birthdate(df['تاریخ تولد'][0]) == True
#
# # تست سناریوهای منفی (Invalid Test Cases)
# def test_invalid_cases(df):
#     # شماره تلفن کمتر از 11 رقم
#     assert validate_phone_number(df['شماره تلفن'][0][:-1]) == False
#     # شماره تلفن بیشتر از 11 رقم
#     assert validate_phone_number(df['شماره تلفن'][0] + '1') == False
#     # شماره تلفن شامل کاراکترهای غیر عددی
#     assert validate_phone_number(df['شماره تلفن'][0][:-1] + 'A') == False
#     # کد ملی کمتر از 10 رقم
#     assert validate_national_id(df['کد ملی'][0][:-1]) == False
#     # کد ملی بیشتر از 10 رقم
#     assert validate_national_id(df['کد ملی'][0] + '1') == False
#     # کد ملی شامل کاراکترهای غیر عددی
#     assert validate_national_id(df['کد ملی'][0][:-1] + 'A') == False
#     # تاریخ تولد فرمت نادرست
#     assert validate_birthdate('2025-30-15') == False
#     # تاریخ تولد بیش از 120 سال پیش (سن غیر معقول)
#     assert validate_birthdate('1800-01-01') == False
#     # تاریخ تولد در آینده
#     assert validate_birthdate('2025-01-01') == False
#
#
# # اجرای تست‌ها برای هر دیتاست
#
# print("اجرای تست‌های مثبت برای دیتاست اول:")
# test_valid_cases(df1)
# print("تست‌های مثبت برای دیتاست اول با موفقیت گذشتند.")
#
# print("\nاجرای تست‌های منفی برای دیتاست اول:")
# test_invalid_cases(df1)
# print("تست‌های منفی برای دیتاست اول با موفقیت گذشتند.")
#
# print("\nاجرای تست‌های مثبت برای دیتاست دوم:")
# test_valid_cases(df2)
# print("تست‌های مثبت برای دیتاست دوم با موفقیت گذشتند.")
#
# print("\nاجرای تست‌های منفی برای دیتاست دوم:")
# test_invalid_cases(df2)
# print("تست‌های منفی برای دیتاست دوم با موفقیت گذشتند.")
#
# print("\nاجرای تست‌های مثبت برای دیتاست سوم:")
# test_valid_cases(df3)
# print("تست‌های مثبت برای دیتاست سوم با موفقیت گذشتند.")
#
# print("\nاجرای تست‌های منفی برای دیتاست سوم:")
# test_invalid_cases(df3)
# print("تست‌های منفی برای دیتاست سوم با موفقیت گذشتند.")0

import time
import requests
import json
import pandas as pd

# داده‌های ثابت برای هر دیتاست
data_1 = {
    'شماره تلفن': ['09356325523'],
    'کد ملی': ['1234567890'],
    'تاریخ تولد': ['1375-03-23'],
    'شماره کارت بانکی': ['6219861083193887']
}

data_2 = {
    'شماره تلفن': ['09331474147'],
    'کد ملی': ['9876543210'],
    'تاریخ تولد': ['1375-03-23'],
    'شماره کارت بانکی': ['5022567880989087']
}

data_3 = {
    'شماره تلفن': ['09182224373'],
    'کد ملی': ['6789012345'],
    'تاریخ تولد': ['1375-03-23'],
    'شماره کارت بانکی': ['6219861083193887']
}

# ایجاد دیتاست‌ها
df1 = pd.DataFrame(data_1)
df2 = pd.DataFrame(data_2)
df3 = pd.DataFrame(data_3)


# تابع برای ثبت کاربر
def register_user(phone_number_or_email: str):
    url = "https://api-staging.tabdealbot.com/register/"
    payload = json.dumps({"phone_or_email": phone_number_or_email})
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=payload)
    response_json = response.json()
    print(response_json["message"])


# تابع برای ارسال درخواست OTP
def send_otp_request(phone_number_or_email, request_type):
    url = f"https://api-staging.tabdealbot.com/utils/staging/otp/?cell_phone={phone_number_or_email}&type={request_type}"

    payload = json.dumps({
        "phone_or_email": phone_number_or_email
    })

    headers = {
        'cell_phone': phone_number_or_email,
        'type': request_type,
        'Content-Type': 'application/json',
        'Cookie': 'TS01933b4f=0150a3e24ed60eb4bc2d06d9173794134de896feaf5fd49ea9095471827d28cd0d11f6ebbe20903a709ab0c2b96c19ed687039b868'
    }

    response = requests.get(url, headers=headers, data=payload)

    try:
        response_data = response.json()
        otp = response_data.get("otp", "")  # استخراج مقدار OTP
        if otp:
            print(otp)
        return response_data
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response"}


# تابع برای ثبت کاربر و دریافت OTP
def register_user_get_otp(phone_number_or_email):
    result = send_otp_request(phone_number_or_email, "Registration")
    otp = result.get("otp", "")

    if not otp:
        print("Error: OTP not received")
        return None

    url = "https://api-staging.tabdealbot.com/register/"
    payload = json.dumps({
        "phone": phone_number_or_email,  # شماره تلفن
        "token": otp,
        "password": 'A@123456789'
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, headers=headers, data=payload)

    if response.status_code == 200:
        response_json = response.json()
        return response_json.get('token')
    else:
        print("Error:", response.text)
        return None


# تابع برای تایید اعتبار
def verify_credentials(national_code, birth_date, card_number, token):
    url = "https://api-staging.tabdealbot.com/verification/credentials/"
    payload = json.dumps({
        "national_code": national_code,
        "birth_date": birth_date,
        "card_number": card_number
    })
    headers = {
        'Authorization': f'HHRAA {token}',
        'Content-Type': 'application/json'
    }
    response = requests.put(url, headers=headers, data=payload)
    print(token)
    print("\n")
    print("Verification Status Code:", response.status_code)
    print(response.text)


# تابع برای دریافت اطلاعات تریدر
def get_trader_info(token):
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
            'Authorization': f'HHRAA {token}',
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

        time.sleep(30)  # توقف 10 ثانیه‌ای بین اجراها


# اجرا کردن کد برای هر دیتاست

if __name__ == '__main__':
    # دیتاست اول
    phone_or_email = df1['شماره تلفن'][0]  # شماره تلفن از دیتاست 1
    register_user(phone_or_email)

    token = register_user_get_otp(phone_or_email)

    national_code = df1['کد ملی'][0]  # کد ملی از دیتاست 1
    card_number = df1['شماره کارت بانکی'][0]  # شماره کارت بانکی از دیتاست 1
    birth_date = df1['تاریخ تولد'][0]  # تاریخ تولد از دیتاست 1

    verify_credentials(national_code, birth_date, card_number, token)
    get_trader_info(token)

    # دیتاست دوم
    phone_or_email = df2['شماره تلفن'][0]  # شماره تلفن از دیتاست 2
    register_user(phone_or_email)

    token = register_user_get_otp(phone_or_email)

    national_code = df2['کد ملی'][0]  # کد ملی از دیتاست 2
    card_number = df2['شماره کارت بانکی'][0]  # شماره کارت بانکی از دیتاست 2
    birth_date = df2['تاریخ تولد'][0]  # تاریخ تولد از دیتاست 2

    verify_credentials(national_code, birth_date, card_number, token)
    get_trader_info(token)

    # دیتاست سوم
    phone_or_email = df3['شماره تلفن'][0]  # شماره تلفن از دیتاست 3
    register_user(phone_or_email)

    token = register_user_get_otp(phone_or_email)

    national_code = df3['کد ملی'][0]  # کد ملی از دیتاست 3
    card_number = df3['شماره کارت بانکی'][0]  # شماره کارت بانکی از دیتاست 3
    birth_date = df3['تاریخ تولد'][0]  # تاریخ تولد از دیتاست 3

    verify_credentials(national_code, birth_date, card_number, token)
    get_trader_info(token)
