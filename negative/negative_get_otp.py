import requests
import json

url = "https://api-staging.tabdealbot.com/register/"
headers = {
    'Content-Type': 'application/json',
    'Cookie': 'TS01933b4f=0150a3e24eac000bc73af795c7336396cfbb53b1f6b3babfdd24f7faf54586669bf23f6d30133e9104f4c2a4d748564846f7f2dadc'
}

def invalid_phone_number():
    payload = json.dumps({
        "phone": "09104",
        "token": "66314",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 1 (Invalid phone number):", response.status_code, response.text)

def weak_password():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "66314",
        "password": "123"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 2 (Weak password):", response.status_code, response.text)

def invalid_token():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "invalid_token",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 3 (Invalid token):", response.status_code, response.text)

def empty_fields():
    payload = json.dumps({
        "phone": "",
        "token": "",
        "password": ""
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 4 (Empty fields):", response.status_code, response.text)

def existing_phone_number():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "66314",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 5 (Existing phone number):", response.status_code, response.text)

def invalid_token_format():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "66314invalid",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 6 (Invalid token format):", response.status_code, response.text)

def invalid_cookie():
    headers_invalid_cookie = {
        'Content-Type': 'application/json',
        'Cookie': 'invalid_cookie_value'
    }
    payload = json.dumps({
        "phone": "09104491104",
        "token": "66314",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers_invalid_cookie, data=payload)
    print("Test case 7 (Invalid cookie):", response.status_code, response.text)

def invalid_content_type():
    headers_invalid_content_type = {
        'Content-Type': 'text/plain',
        'Cookie': 'TS01933b4f=0150a3e24eac000bc73af795c7336396cfbb53b1f6b3babfdd24f7faf54586669bf23f6d30133e9104f4c2a4d748564846f7f2dadc'
    }
    payload = json.dumps({
        "phone": "09104491104",
        "token": "66314",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers_invalid_content_type, data=payload)
    print("Test case 8 (Invalid content type):", response.status_code, response.text)

def run_negative_register_get_otp_tests():
    invalid_phone_number()
    weak_password()
    invalid_token()
    empty_fields()
    existing_phone_number()
    invalid_token_format()
    invalid_cookie()
    invalid_content_type()

run_negative_register_get_otp_tests()
