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

def existing_phone_number():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "66314",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 2 (Existing phone number):", response.status_code, response.text)



def invalid_phone_number_short():
    payload = json.dumps({
        "phone": "09104",
        "token": "66314",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 3 (Phone number too short):", response.status_code, response.text)


def invalid_phone_number_long():
    payload = json.dumps({
        "phone": "091041234567890",  # بیشتر از 10 رقم
        "token": "66314",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 4 (Phone number too long):", response.status_code, response.text)


def invalid_phone_number_non_numeric():
    payload = json.dumps({
        "phone": "0910A12345",  # حاوی کاراکتر غیر عددی
        "token": "66314",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    response_json = json.loads(response.text)

    print("Test case 5 (Non-numeric characters in phone number):", response.status_code, response_json["detail"])



def invalid_phone_number_special_chars():
    payload = json.dumps({
        "phone": "0910-12345",
        "token": "66314",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    response_json = json.loads(response.text)

    print("Test case 6 (Special characters in phone number):", response.status_code, response_json["detail"])


def invalid_phone_number_format():
    payload = json.dumps({
        "phone": "0910 123 45",
        "token": "66314",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)

    response_json = json.loads(response.text)

    print("Test case 7 (Incorrect format with spaces):", response.status_code, response_json["detail"])

invalid_phone_number_format()


def invalid_phone_number_country_code():
    payload = json.dumps({
        "phone": "+989104123456",
        "token": "66314",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 8 (Incorrect country code):", response.status_code, response.text)


def invalid_phone_number_empty():
    payload = json.dumps({
        "phone": "",  # شماره تلفن خالی
        "token": "66314",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    response_json = json.loads(response.text)

    print("Test case 9 (Empty phone number):", response.status_code,response_json["detail"])

def invalid_phone_number_repeated_digits():
    payload = json.dumps({
        "phone": "1111111111",
        "token": "66314",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 10 (Repeated digits in phone number):", response.status_code, response.text)


def invalid_phone_number_sequential_digits():
    payload = json.dumps({
        "phone": "0123456789",
        "token": "66314",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 11 (Sequential digits in phone number):", response.status_code, response.text)


def invalid_token():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "invalid_token",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 12 (Invalid token):", response.status_code, response.text)


def empty_fields():
    payload = json.dumps({
        "phone": "",
        "token": "",
        "password": ""
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 13 (Empty fields):", response.status_code, response.text)


def long_token():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "a" * 1000,
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 14 (Long token):", response.status_code, response.text)


def token_with_special_characters():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "invalid@token#123!",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 15 (Token with special characters):", response.status_code, response.text)


def incorrect_format_token():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "abc123xyz",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 16 (Incorrect format token):", response.status_code, response.text)


def token_with_whitespace():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "  invalid_token  ",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 17 (Token with whitespace):", response.status_code, response.text)


def case_sensitive_token():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "INVALID_token",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 18 (Case-sensitive token):", response.status_code, response.text)


def expired_token():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "expired_token_12345",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 19 (Expired token):", response.status_code, response.text)


def incorrect_token_for_phone():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "wrong_token_for_this_phone",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 20 (Incorrect token for phone):", response.status_code, response.text)


def invalid_token_format():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "66314invalid",
        "password": "Keshavarz007007"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 21 (Invalid token format):", response.status_code, response.text)




def weak_password():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "66314",
        "password": "123"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 22 (Weak password):", response.status_code, response.text)


def short_password():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "66314",
        "password": "12"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 23 (Short password):", response.status_code, response.text)

def no_uppercase_password():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "66314",
        "password": "password123"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 24 (No uppercase letter in password):", response.status_code, response.text)

def no_number_password():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "66314",
        "password": "password"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 25 (No number in password):", response.status_code, response.text)

def no_special_characters_password():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "66314",
        "password": "Password123"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 26 (No special characters in password):", response.status_code, response.text)

def long_password():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "66314",
        "password": "a" * 1000
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 27 (Long password):", response.status_code, response.text)

def password_with_whitespace():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "66314",
        "password": "  password123  "
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 28 (Password with whitespace):", response.status_code, response.text)

def predictable_password():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "66314",
        "password": "password123"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 29 (Predictable password):", response.status_code, response.text)

def all_numeric_password():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "66314",
        "password": "12345678"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 30 (All numeric password):", response.status_code, response.text)

def special_characters_only_password():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "66314",
        "password": "!@#$%^&*"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 31 (Special characters only password):", response.status_code, response.text)

def invalid_characters_in_password():
    payload = json.dumps({
        "phone": "09104491104",
        "token": "66314",
        "password": "پاسورد123"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 32 (Invalid characters in password):", response.status_code, response.text)



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
    print("Test case 33 (Invalid cookie):", response.status_code, response.text)

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
    print("Test case 34 (Invalid content type):", response.status_code, response.text)





def run_negative_register_get_otp_tests():
    def run_negative_register_get_otp_tests():
        invalid_phone_number()
        existing_phone_number()
        invalid_phone_number_short()
        invalid_phone_number_long()
        invalid_phone_number_non_numeric()
        invalid_phone_number_special_chars()
        invalid_phone_number_format()
        invalid_phone_number_country_code()
        invalid_phone_number_empty()
        invalid_phone_number_repeated_digits()
        invalid_phone_number_sequential_digits()


        invalid_token()
        empty_fields()
        long_token()
        token_with_special_characters()
        incorrect_format_token()
        token_with_whitespace()
        case_sensitive_token()
        expired_token()
        incorrect_token_for_phone()
        invalid_token_format()


        weak_password()
        short_password()
        no_uppercase_password()
        no_number_password()
        no_special_characters_password()
        long_password()
        password_with_whitespace()
        predictable_password()
        all_numeric_password()
        special_characters_only_password()
        invalid_characters_in_password()


        invalid_cookie()
        invalid_content_type()

    run_negative_register_get_otp_tests()

run_negative_register_get_otp_tests()
