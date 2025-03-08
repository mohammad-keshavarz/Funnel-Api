import requests
import json

url = "https://api-staging.tabdealbot.com/verification/credentials/"

headers = {
    'Authorization': 'abc',
    'Content-Type': 'application/json'
}

def missing_fields():
    payload = json.dumps({})  # No fields provided
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 1 (Missing fields):", response.status_code, response.text)

def invalid_national_code():
    payload = json.dumps({
        "national_code": "123",  # Invalid national code (too short)
        "birth_date": "1375-03-22",
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 2 (Invalid national code):", response.status_code, response.text)


def national_code_non_numeric():
    payload = json.dumps({
        "national_code": "ABC123XYZ",
        "birth_date": "1375-03-22",
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 3  (National code contains non-numeric characters):", response.status_code, response.text)

def national_code_special_characters():
    payload = json.dumps({
        "national_code": "40612@#$%",
        "birth_date": "1375-03-22",
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 4 (National code contains special characters):", response.status_code, response.text)

def national_code_invalid_checksum():
    payload = json.dumps({
        "national_code": "4061246268",  # کد ملی با چکسام نادرست
        "birth_date": "1375-03-22",
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 5 (Invalid national code checksum):", response.status_code, response.text)

def national_code_leading_zeros():
    payload = json.dumps({
        "national_code": "0001246267",  # شروع با صفرهای غیرعادی
        "birth_date": "1375-03-22",
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 6 (National code with leading zeros):", response.status_code, response.text)

def national_code_all_same_digits():
    payload = json.dumps({
        "national_code": "1111111111",  # تمام ارقام یکسان
        "birth_date": "1375-03-22",
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 7 (National code with all same digits):", response.status_code, response.text)

def national_code_whitespace():
    payload = json.dumps({
        "national_code": "40612 46267",  # دارای فاصله بین ارقام
        "birth_date": "1375-03-22",
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 8 (National code with whitespace):", response.status_code, response.text)


def invalid_birth_date_format():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "75/03/22",
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 9 (Invalid birth date format):", response.status_code, response.text)


def birth_date_missing():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "",  # تاریخ تولد خالی
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 10 (Birth date missing):", response.status_code, response.text)

def birth_date_future():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "1500-01-01",  # تاریخ در آینده
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 11 (Birth date in the future):", response.status_code, response.text)

def birth_date_past_limit():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "1200-01-01",  # تاریخ خیلی قدیمی
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 12 (Birth date too far in the past):", response.status_code, response.text)

def birth_date_non_numeric():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "abcd-ef-gh",
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 13 (Non-numeric birth date):", response.status_code, response.text)

def birth_date_wrong_format():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "22-03-1375",
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 13 (Wrong birth date format):", response.status_code, response.text)

def birth_date_month_out_of_range():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "1375-13-10",  # ماه غیرمجاز
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 14 (Month out of range):", response.status_code, response.text)

def birth_date_day_out_of_range():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "1375-03-32",  # روز غیرمجاز
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 15 (Day out of range):", response.status_code, response.text)

def birth_date_invalid_leap_year():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "1401-12-30",  # سال غیر کبیسه با روز ۳۰ اسفند
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 16 (Invalid leap year date):", response.status_code, response.text)

def birth_date_special_characters():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "@#$%-03-22",  # شامل کاراکترهای خاص
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 17 (Special characters in birth date):", response.status_code, response.text)

def birth_date_numeric_but_invalid():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "9999-99-99",  # تاریخ عددی ولی غیرواقعی
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 18 (Completely invalid numeric date):", response.status_code, response.text)

def birth_date_text_instead_of_date():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "March 22, 1996",  # فرمت انگلیسی
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 19 (Text format instead of date):", response.status_code, response.text)


def invalid_card_number():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "1375-03-22",
        "card_number": "123456"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 20 (Invalid card number):", response.status_code, response.text)



def card_number_missing():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "1375-03-22",
        "card_number": ""  # شماره کارت خالی
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 20 (Card number missing):", response.status_code, response.text)

def card_number_too_short():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "1375-03-22",
        "card_number": "50222913"  # کمتر از ۱۶ رقم
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 21 (Card number too short):", response.status_code, response.text)

def card_number_too_long():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "1375-03-22",
        "card_number": "502229132062488399"  # بیشتر از ۱۶ رقم
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 22 (Card number too long):", response.status_code, response.text)

def card_number_non_numeric():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "1375-03-22",
        "card_number": "5022A913206B4883"  # شامل حروف
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 23 (Card number contains non-numeric characters):", response.status_code, response.text)

def card_number_special_characters():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "1375-03-22",
        "card_number": "5022-2913-2062-4883"  # شامل کاراکترهای خاص
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 24 (Card number contains special characters):", response.status_code, response.text)

def card_number_invalid_checksum():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "1375-03-22",
        "card_number": "5022291320624884"  # شماره کارت با چکسام نامعتبر
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 25 (Invalid card number checksum):", response.status_code, response.text)

def card_number_leading_zeros():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "1375-03-22",
        "card_number": "0000291320624883"  # شروع با صفرهای غیرعادی
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 26 (Card number with leading zeros):", response.status_code, response.text)

def card_number_all_same_digits():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "1375-03-22",
        "card_number": "1111111111111111"  # تمام ارقام یکسان
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 27 (Card number with all same digits):", response.status_code, response.text)

def card_number_whitespace():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "1375-03-22",
        "card_number": "5022 2913 2062 4883"  # دارای فاصله بین ارقام
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 28 (Card number with whitespace):", response.status_code, response.text)

def empty_fields():
    payload = json.dumps({
        "national_code": "",
        "birth_date": "",
        "card_number": ""
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 29 (Empty fields):", response.status_code, response.text)

def invalid_token():
    headers_invalid_auth = {
        'Authorization': 'invalid_token',
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "1375-03-22",
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers_invalid_auth, data=payload)
    print("Test case 30 (Invalid token):", response.status_code, response.text)

def missing_auth_header():
    headers_no_auth = {
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "1375-03-22",
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers_no_auth, data=payload)
    print("Test case 31 (Missing Authorization header):", response.status_code, response.text)

def invalid_http_method():
    payload = json.dumps({
        "national_code": "4061246267",
        "birth_date": "1375-03-22",
        "card_number": "5022291320624883"
    })
    response = requests.post(url, headers=headers, data=payload)  # Using POST instead of PUT
    print("Test case 32 (Invalid HTTP method):", response.status_code, response.text)

def large_payload():
    payload = json.dumps({
        "national_code": "4061246267" * 1000,  # Extremely long national code
        "birth_date": "1375-03-22",
        "card_number": "5022291320624883"
    })
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 33 (Large payload size):", response.status_code, response.text)

def malformed_json():
    payload = '{"national_code": "4061246267", "birth_date": "1375-03-22", "card_number": "5022291320624883"'  # Missing closing brace
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 33 (Malformed JSON):", response.status_code, response.text)


def run_negative_verification_tests():
    missing_fields()
    invalid_national_code()
    national_code_non_numeric()
    national_code_special_characters()
    national_code_invalid_checksum()
    national_code_leading_zeros()
    national_code_all_same_digits()
    national_code_whitespace()

    invalid_birth_date_format()
    birth_date_missing()
    birth_date_future()
    birth_date_past_limit()
    birth_date_non_numeric()
    birth_date_wrong_format()
    birth_date_month_out_of_range()
    birth_date_day_out_of_range()
    birth_date_invalid_leap_year()
    birth_date_special_characters()
    birth_date_numeric_but_invalid()
    birth_date_text_instead_of_date()

    invalid_card_number()
    card_number_missing()
    card_number_too_short()
    card_number_too_long()
    card_number_non_numeric()
    card_number_special_characters()
    card_number_invalid_checksum()
    card_number_leading_zeros()
    card_number_all_same_digits()
    card_number_whitespace()

    empty_fields()
    invalid_token()
    missing_auth_header()
    invalid_http_method()
    large_payload()
    malformed_json()


run_negative_verification_tests()
