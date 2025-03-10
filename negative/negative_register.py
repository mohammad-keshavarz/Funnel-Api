import requests
import json


url = "https://api-staging.tabdealbot.com/register/"
headers = {
    'Content-Type': 'application/json',
    'Cookie': 'TS01933b4f=0150a3e24eac000bc73af795c7336396cfbb53b1f6b3babfdd24f7faf54586669bf23f6d30133e9104f4c2a4d748564846f7f2dadc'
}


def missing_phone_or_email():
    payload = json.dumps({
        "phone_or_email": ""
    })
    response = requests.post(url, headers=headers, data=payload)
    print("Test case 1 (missing_phone_or_email):", response.status_code, response.text)

def space_phone_or_email():
    payload = json.dumps({
        "phone_or_email": "    "
    })
    response = requests.post(url, headers=headers, data=payload)
    print("Test case 2 (space_phone_or_email):", response.status_code, response.text)

def invalid_phone_format():
    payload = json.dumps({
        "phone_or_email": "09104"
    })
    response = requests.post(url, headers=headers, data=payload)
    print("Test case 3 (invalid_phone_format):", response.status_code, response.text)


def xss_injection():
    xss_input = "<script>alert('XSS')</script>"
    payload = json.dumps({
        "phone_or_email": xss_input,

    })
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        print(f"Test failed. XSS input '{xss_input}' should have been blocked.")
    else:
        print(f"Test case 4 (Error caught as expected for XSS injection): {response.status_code} - {response.text}")



def csrf_protection():
    csrf_attack_input = {
        "phone_or_email": "attacker@example.com",
        "token": "attacker_token",  # ------->  اینجا مثلا یه هکر با توکن غیر معتبر سعی در نفوذ داره
        "password": "securePassword123"
    }
    payload = json.dumps(csrf_attack_input)
    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        print("Test failed. CSRF attack should be prevented.")
    else:
        print(f"Test case 6 (Error caught as expected for CSRF attack): {response.status_code} - {response.text}")


def run_negative_register_tests():

    missing_phone_or_email()
    space_phone_or_email()
    invalid_phone_format()
    xss_injection()


run_negative_register_tests()
