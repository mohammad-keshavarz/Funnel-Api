

import requests
import json
import random

# تعریف لیست برای ذخیره شماره‌های تولید شده
generated_numbers = set()

def generate_unique_phone_number():
    while True:
        operator_code = random.randint(10, 99)  # کد اپراتور (دو رقمی)
        subscriber_number = random.randint(0, 9999999)  # شماره مشترک (7 رقمی)
        phone_number = f"09{operator_code:02d}{subscriber_number:07d}"
        if phone_number not in generated_numbers:
            generated_numbers.add(phone_number)
            return phone_number

def register_user(phone_number_or_email: str):
    # دریافت شماره تلفن منحصر به فرد
    url = "https://api-staging.tabdealbot.com/register/"

    payload = json.dumps({
        "phone_or_email": phone_number_or_email
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'TS01933b4f=0150a3e24e4d8d2e8efca8329e6ddbd82c80ec35a8f9d6ede8de18b9e0d96b5089a836245889cd1f9ef758328b58627894d46f37cd'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)




def register_user_get_otp(phone_number_or_email):
    url = "https://api-staging.tabdealbot.com/register/"

    payload = json.dumps({
        "phone": phone_number_or_email,
        "token": input('Enter Token: '),
        "password": 'harchi'
    })

    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'TS01933b4f=0150a3e24e4d8d2e8efca8329e6ddbd82c80ec35a8f9d6ede8de18b9e0d96b5089a836245889cd1f9ef758328b58627894d46f37cd'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.text )
    response_json = response.json()

    token = response_json.get('token')
    # چاپ فقط token
    print(token)







if __name__ == '__main__':
    phone_or_email = generate_unique_phone_number()
    register_user(phone_or_email)
    print(register_user_get_otp(phone_or_email))
