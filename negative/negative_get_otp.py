# # import requests
# # import json
# #
# # url = "https://api-staging.tabdealbot.com/register/"
# # headers = {
# #     'Content-Type': 'application/json',
# #     'Cookie': 'TS01933b4f=0150a3e24eac000bc73af795c7336396cfbb53b1f6b3babfdd24f7faf54586669bf23f6d30133e9104f4c2a4d748564846f7f2dadc'
# # }
# #
# # def invalid_phone_number():
# #     payload = json.dumps({
# #         "phone": "09104",
# #         "token": "66314",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 1 (Invalid phone number):", response.status_code, response.text)
# #
# # def existing_phone_number():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "66314",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 2 (Existing phone number):", response.status_code, response.text)
# #
# #
# #
# # def invalid_phone_number_short():
# #     payload = json.dumps({
# #         "phone": "09104",
# #         "token": "66314",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 3 (Phone number too short):", response.status_code, response.text)
# #
# #
# # def invalid_phone_number_long():
# #     payload = json.dumps({
# #         "phone": "091041234567890",  # بیشتر از 10 رقم
# #         "token": "66314",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 4 (Phone number too long):", response.status_code, response.text)
# #
# #
# # def invalid_phone_number_non_numeric():
# #     payload = json.dumps({
# #         "phone": "0910A12345",  # حاوی کاراکتر غیر عددی
# #         "token": "66314",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     response_json = json.loads(response.text)
# #
# #     print("Test case 5 (Non-numeric characters in phone number):", response.status_code, response_json["detail"])
# #
# #
# #
# # def invalid_phone_number_special_chars():
# #     payload = json.dumps({
# #         "phone": "0910-12345",
# #         "token": "66314",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     response_json = json.loads(response.text)
# #
# #     print("Test case 6 (Special characters in phone number):", response.status_code, response_json["detail"])
# #
# #
# # def invalid_phone_number_format():
# #     payload = json.dumps({
# #         "phone": "0910 123 45",
# #         "token": "66314",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #
# #     response_json = json.loads(response.text)
# #
# #     print("Test case 7 (Incorrect format with spaces):", response.status_code, response_json["detail"])
# #
# # invalid_phone_number_format()
# #
# #
# # def invalid_phone_number_country_code():
# #     payload = json.dumps({
# #         "phone": "+989104123456",
# #         "token": "66314",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 8 (Incorrect country code):", response.status_code, response.text)
# #
# #
# # def invalid_phone_number_empty():
# #     payload = json.dumps({
# #         "phone": "",  # شماره تلفن خالی
# #         "token": "66314",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     response_json = json.loads(response.text)
# #
# #     print("Test case 9 (Empty phone number):", response.status_code,response_json["detail"])
# #
# # def invalid_phone_number_repeated_digits():
# #     payload = json.dumps({
# #         "phone": "1111111111",
# #         "token": "66314",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 10 (Repeated digits in phone number):", response.status_code, response.text)
# #
# #
# # def invalid_phone_number_sequential_digits():
# #     payload = json.dumps({
# #         "phone": "0123456789",
# #         "token": "66314",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 11 (Sequential digits in phone number):", response.status_code, response.text)
# #
# #
# # def invalid_token():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "invalid_token",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 12 (Invalid token):", response.status_code, response.text)
# #
# #
# # def empty_fields():
# #     payload = json.dumps({
# #         "phone": "",
# #         "token": "",
# #         "password": ""
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 13 (Empty fields):", response.status_code, response.text)
# #
# #
# # def long_token():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "a" * 1000,
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 14 (Long token):", response.status_code, response.text)
# #
# #
# # def token_with_special_characters():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "invalid@token#123!",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 15 (Token with special characters):", response.status_code, response.text)
# #
# #
# # def incorrect_format_token():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "abc123xyz",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 16 (Incorrect format token):", response.status_code, response.text)
# #
# #
# # def token_with_whitespace():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "  invalid_token  ",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 17 (Token with whitespace):", response.status_code, response.text)
# #
# #
# # def case_sensitive_token():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "INVALID_token",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 18 (Case-sensitive token):", response.status_code, response.text)
# #
# #
# # def expired_token():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "expired_token_12345",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 19 (Expired token):", response.status_code, response.text)
# #
# #
# # def incorrect_token_for_phone():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "wrong_token_for_this_phone",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 20 (Incorrect token for phone):", response.status_code, response.text)
# #
# #
# # def invalid_token_format():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "66314invalid",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 21 (Invalid token format):", response.status_code, response.text)
# #
# #
# #
# #
# # def weak_password():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "66314",
# #         "password": "123"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 22 (Weak password):", response.status_code, response.text)
# #
# #
# # def short_password():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "66314",
# #         "password": "12"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 23 (Short password):", response.status_code, response.text)
# #
# # def no_uppercase_password():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "66314",
# #         "password": "password123"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 24 (No uppercase letter in password):", response.status_code, response.text)
# #
# # def no_number_password():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "66314",
# #         "password": "password"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 25 (No number in password):", response.status_code, response.text)
# #
# # def no_special_characters_password():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "66314",
# #         "password": "Password123"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 26 (No special characters in password):", response.status_code, response.text)
# #
# # def long_password():
# #     payload = json.dumps({
# #         "phone": "9191695389",
# #         "token": "29836",
# #         "password": "a" * 1000
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 27 (Long password):", response.status_code, response.text)
# #
# # def password_with_whitespace():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "66314",
# #         "password": "  password123  "
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 28 (Password with whitespace):", response.status_code, response.text)
# #
# # def predictable_password():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "66314",
# #         "password": "password123"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 29 (Predictable password):", response.status_code, response.text)
# #
# # def all_numeric_password():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "66314",
# #         "password": "12345678"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 30 (All numeric password):", response.status_code, response.text)
# #
# # def special_characters_only_password():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "66314",
# #         "password": "!@#$%^&*"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 31 (Special characters only password):", response.status_code, response.text)
# #
# # def invalid_characters_in_password():
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "66314",
# #         "password": "پاسورد123"
# #     })
# #     response = requests.put(url, headers=headers, data=payload)
# #     print("Test case 32 (Invalid characters in password):", response.status_code, response.text)
# #
# #
# #
# # def invalid_cookie():
# #     headers_invalid_cookie = {
# #         'Content-Type': 'application/json',
# #         'Cookie': 'invalid_cookie_value'
# #     }
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "66314",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers_invalid_cookie, data=payload)
# #     print("Test case 33 (Invalid cookie):", response.status_code, response.text)
# #
# # def invalid_content_type():
# #     headers_invalid_content_type = {
# #         'Content-Type': 'text/plain',
# #         'Cookie': 'TS01933b4f=0150a3e24eac000bc73af795c7336396cfbb53b1f6b3babfdd24f7faf54586669bf23f6d30133e9104f4c2a4d748564846f7f2dadc'
# #     }
# #     payload = json.dumps({
# #         "phone": "09104491104",
# #         "token": "66314",
# #         "password": "Keshavarz007007"
# #     })
# #     response = requests.put(url, headers=headers_invalid_content_type, data=payload)
# #     print("Test case 34 (Invalid content type):", response.status_code, response.text)
# #
# #
# #
# #
# #
# # def run_negative_register_get_otp_tests():
# #     def run_negative_register_get_otp_tests():
# #         invalid_phone_number()
# #         existing_phone_number()
# #         invalid_phone_number_short()
# #         invalid_phone_number_long()
# #         invalid_phone_number_non_numeric()
# #         invalid_phone_number_special_chars()
# #         invalid_phone_number_format()
# #         invalid_phone_number_country_code()
# #         invalid_phone_number_empty()
# #         invalid_phone_number_repeated_digits()
# #         invalid_phone_number_sequential_digits()
# #
# #
# #         invalid_token()
# #         empty_fields()
# #         long_token()
# #         token_with_special_characters()
# #         incorrect_format_token()
# #         token_with_whitespace()
# #         case_sensitive_token()
# #         expired_token()
# #         incorrect_token_for_phone()
# #         invalid_token_format()
# #
# #
# #         weak_password()
# #         short_password()
# #         no_uppercase_password()
# #         no_number_password()
# #         no_special_characters_password()
# #         long_password()
# #         password_with_whitespace()
# #         predictable_password()
# #         all_numeric_password()
# #         special_characters_only_password()
# #         invalid_characters_in_password()
# #
# #
# #         invalid_cookie()
# #         invalid_content_type()
# #
# #     run_negative_register_get_otp_tests()
# #
# # run_negative_register_get_otp_tests()
#
# import requests
# import json
# import random
#
# generated_numbers = set()
# def generate_unique_phone_number():
#     while True:
#         operator_code = random.randint(10, 99)
#         subscriber_number = random.randint(0, 9999999)
#         phone_number = f"09{operator_code:02d}{subscriber_number:07d}"
#         if phone_number not in generated_numbers:
#             generated_numbers.add(phone_number)
#             return phone_number
#
#
# generated_codes = set()
# def generate_national_Code_id():
#     while True:
#         first_nine_digits = [random.randint(0, 9) for _ in range(9)]
#         checksum = sum((10 - i) * first_nine_digits[i] for i in range(9)) % 11
#         control_digit = checksum if checksum < 2 else 11 - checksum
#         national_id = "".join(map(str, first_nine_digits)) + str(control_digit)
#
#         if national_id not in generated_codes:
#             generated_codes.add(national_id)
#             return national_id
#
#
# generated_cards = set()
# def logic_card_number(card_number):
#     digits = [int(d) for d in card_number]
#     for i in range(0, 15, 2):
#         digits[i] *= 2
#         if digits[i] > 9:
#             digits[i] -= 9
#     return (10 - sum(digits) % 10) % 10
#
# def generate_bank_card():
#     while True:
#         bank_prefix = random.choice(["6037", "5892", "6274", "6221", "5022", "6219", "6393", "5859"])
#         random_digits = [random.randint(0, 9) for _ in range(11)]
#         partial_card_number = bank_prefix + "".join(map(str, random_digits))
#         control_digit = logic_card_number(partial_card_number + "0")
#         full_card_number = partial_card_number + str(control_digit)
#
#         if full_card_number not in generated_cards:
#             generated_cards.add(full_card_number)
#             return full_card_number
#
#
# def register_user(phone_number_or_email: str):
#     url = "https://api-staging.tabdealbot.com/register/"
#     payload = json.dumps({"phone_or_email": phone_number_or_email})
#     headers = {'Content-Type': 'application/json'}
#     response = requests.post(url, headers=headers, data=payload)
#     response_json = response.json()
#     print(response_json["message"])
#     # print(response.text)
#
#
# def register_user_get_otp(phone_number_or_email):
#     get_input_from_user = input('Enter OTP: ')
#
#     url = "https://api-staging.tabdealbot.com/register/"
#     payload = json.dumps({
#         "phone": phone_number_or_email,
#         "token": get_input_from_user,
#         "password": 'A@123456789'
#     })
#     headers = {'Content-Type': 'application/json'}
#     response = requests.put(url, headers=headers, data=payload)
#     print(get_input_from_user)
#
#     if response.status_code == 200:
#         response_json = response.json()
#         return response_json.get('token')
#     else:
#         print("Error:", response.text)
#         return None
#
# def verify_credentials(national_code, birth_date, card_number, token):
#     url = "https://api-staging.tabdealbot.com/verification/credentials/"
#     payload = json.dumps({
#         "national_code": national_code,
#         "birth_date": birth_date,
#         "card_number": card_number
#     })
#     headers = {
#         'Authorization': f'HHRAA {token}',
#         'Content-Type': 'application/json'
#     }
#     response = requests.put(url, headers=headers, data=payload)
#     print(token)
#     print("\n")
#     print("Verification Status Code:", response.status_code)
#     print(response.text)
#
#
# def get_trader_info():
#     print("#############################  Trader #######################################")
#     url = "https://api-web.tabdeal.org/r/trader/"
#     headers = {
#         "accept": "application/json, text/plain, */*",
#         "accept-language": "fa-ir",
#         "authorization":  f'HHRAA {token}',
#         "origin": "https://api-web.tabdeal.org",
#         "priority": "u=1, i",
#         "referer": "https://api-web.tabdeal.org",
#         "sec-fetch-dest": "empty",
#         "sec-fetch-mode": "cors",
#         "sec-fetch-site": "same-site",
#         "traceparent": "00-11c37ab9558c7c3a39c0ea29d53a58ae-5ed06f0c9aaf2dc5-00",
#         "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
#     }
#
#     response = requests.get(url, headers=headers)
#     print(response.text)
#
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return {"error": f"Request failed with status code {response.status_code}"}
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     phone_or_email = generate_unique_phone_number()
#     register_user(phone_or_email)
#     token = register_user_get_otp(phone_or_email)
#     national_code = generate_national_Code_id()
#     card_number = generate_bank_card()
#     birth_date = "1375-03-23"
#     verify_credentials(national_code, birth_date, card_number, token)
#     get_trader_info()



from dbm import error
import requests
import json
import random


generated_numbers = set()
def generate_unique_phone_number():
    while True:
        operator_code = random.randint(10, 99)
        subscriber_number = random.randint(0, 9999999)
        phone_number = f"09{operator_code:02d}{subscriber_number:07d}"
        if phone_number not in generated_numbers:
            generated_numbers.add(phone_number)
            return phone_number




def register_user(phone_number_or_email: str):

    payload = json.dumps({"phone_or_email": phone_number_or_email})
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=payload)
    response_json = response.json()
    print(response_json["message"])



def register_user_get_otp_with_null_phone_number():
    print("\n")
    print("#######################  INPUT PHONE NUMBER TESTS   #######################)")
    print("\n")
    payload = json.dumps({
        "phone": "",
        "otp": get_otp_input_from_user,
        "password": 'A@123456789'
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 1 (register_user_get_otp_with_null_number):")
    # x = (response.content)
    # decoded_content = x.decode('utf-8')
    # response_json = json.loads(decoded_content)
    # print("پیام خطا:", response_json["error"])

    error_message = response.content.decode('utf-8')


    if response.status_code == 200:
        response_json = response.json()
        return response_json.get('token')
    else:
        print(response.text)
        return None




def register_user_get_otp_with_space_phone_number():

    payload = json.dumps({
        "phone": "        ",
        "otp": get_otp_input_from_user,
        "password": 'A@123456789'
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, headers=headers, data=payload)
    print("\n")
    print("Test case 2:", "register_user_get_otp_with_space_number")
    # print(get_input_from_user)

    if response.status_code == 200:
        response_json = response.json()
        print(response.text)
        return response_json.get('token')
    else:
        print(response.text)
        return None



def register_user_get_otp_with_bad_format_number_phone_number():

    payload = json.dumps({
        "phone": "0910    5915547",
        "otp": get_otp_input_from_user,
        "password": 'A@123456789'
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, headers=headers, data=payload)
    print("\n")
    print("Test case 3:", "register_user_get_otp_with_bad_format_number")
    # print(get_input_from_user)

    if response.status_code == 200:
        response_json = response.json()
        print(response.text)
        return response_json.get('token')
    else:
        print(response.text)
        return None



def xss_injection_in_phone_number():
    xss_input = "<script>alert('XSS')</script>"
    payload = json.dumps({
        "phone_or_email": xss_input,

    })
    response = requests.post(url, headers=headers, data=payload)
    print("\n")
    print(f"Test case 4:", "xss_injection_in_phone_number")
    print(response.text)
    if response.status_code == 200:

        print(f"Test failed. XSS input '{xss_input}' should have been blocked.")
    else:
        pass


    print("\n")
    print("#######################  INPUT otp TESTS   #######################)")


def register_user_get_otp_with_null_OTP():
    print("\n")
    #######################  phone_nimber_test   #######################
    payload = json.dumps({
        "phone": "09102225588",
        "otp": "",
        "password": 'Keshavarz007007'
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 1 (register_user_get_otp_with_null_number):")

    if response.status_code == 200:
        response_json = response.json()
        return response_json.get('token')
    else:
        print(response.text , response.content)
        return None


def register_user_get_otp_with_space_OTP():
    print("\n")

    payload = json.dumps({
        "phone": phone_or_email,
        "otp": "     ",
        "password": 'A@123456789'
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, headers=headers, data=payload)
    print("Test case 2 (register_user_get_otp_with_space_OTP):")

    if response.status_code == 200:
        response_json = response.json()
        return response_json.get('token')
    else:
        print(response.text , response.content)
        return None



if __name__ == '__main__':


    url = "https://api-staging.tabdealbot.com/register/"
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'TS01933b4f=0150a3e24eac000bc73af795c7336396cfbb53b1f6b3babfdd24f7faf54586669bf23f6d30133e9104f4c2a4d748564846f7f2dadc'
    }


    phone_or_email = generate_unique_phone_number()
    register_user(phone_or_email)
    get_otp_input_from_user = input('Enter OTP: ')


    register_user_get_otp_with_null_phone_number()
    register_user_get_otp_with_space_phone_number()
    register_user_get_otp_with_bad_format_number_phone_number()
    xss_injection_in_phone_number()

    register_user_get_otp_with_null_OTP()
    register_user_get_otp_with_space_OTP()