import requests
import json
import random

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
def register_user(phone_number_or_email: str):
    url = "https://api-staging.tabdealbot.com/register/"
    payload = json.dumps({"phone_or_email": ""})
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=payload)
    response_json = response.json()
    print(response_json["message"])
    # print(response.text)


def register_user_get_otp(phone_number_or_email):
    get_input_from_user = input('Enter OTP: ')

    url = "https://api-staging.tabdealbot.com/register/"
    payload = json.dumps({
        "phone": phone_number_or_email,
        "token": get_input_from_user,
        "password": 'A@123456789'
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, headers=headers, data=payload)
    print(get_input_from_user)

    if response.status_code == 200:
        response_json = response.json()
        return response_json.get('token')
    else:
        print("Error:", response.text)
        return None

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


def get_trader_info():
    print("#############################  Trader #######################################")
    url = "https://api-web.tabdeal.org/r/trader/"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "fa-ir",
        "authorization":  f'HHRAA {token}',
        "origin": "https://api-web.tabdeal.org",
        "priority": "u=1, i",
        "referer": "https://api-web.tabdeal.org",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "traceparent": "00-11c37ab9558c7c3a39c0ea29d53a58ae-5ed06f0c9aaf2dc5-00",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
    }

    response = requests.get(url, headers=headers)
    print(response.text)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}"}







if __name__ == '__main__':
    # phone_or_email = generate_unique_phone_number()
    # register_user(phone_or_email)
    # token = register_user_get_otp(phone_or_email)
    # national_code = generate_national_Code_id()
    # card_number = generate_bank_card()
    birth_date = "1375-03-23"
    # verify_credentials(national_code, birth_date, card_number, token)
    get_trader_info()
