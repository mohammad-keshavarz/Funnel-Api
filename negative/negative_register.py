import requests
import json

url = "https://api-staging.tabdealbot.com/register/"


headers = {
    'Content-Type': 'application/json',
    'Cookie': 'TS01933b4f=0150a3e24eac000bc73af795c7336396cfbb53b1f6b3babfdd24f7faf54586669bf23f6d30133e9104f4c2a4d748564846f7f2dadc'
}


def missing_phone_or_email():
    payload = json.dumps({})
    response = requests.post(url, headers=headers, data=payload)
    print("Test case 1 (Missing phone_or_email):", response.status_code, response.text)


def invalid_phone_format():
    payload = json.dumps({
        "phone_or_email": "09104"
    })
    response = requests.post(url, headers=headers, data=payload)
    print("Test case 2 (Invalid phone number format):", response.status_code, response.text)


def invalid_email_format():
    payload = json.dumps({
        "phone_or_email": "invalid-email"
    })
    response = requests.post(url, headers=headers, data=payload)
    print("Test case 3 (Invalid email format):", response.status_code, response.text)


def empty_phone_or_email():
    payload = json.dumps({
        "phone_or_email": ""
    })
    response = requests.post(url, headers=headers, data=payload)
    print("Test case 4 (Empty phone_or_email):", response.status_code, response.text)


def invalid_cookie():
    headers_invalid_cookie = {
        'Content-Type': 'application/json',
        'Cookie': 'invalid_cookie_value'
    }
    payload = json.dumps({
        "phone_or_email": "09104491104"  # Valid phone number
    })
    response = requests.post(url, headers=headers_invalid_cookie, data=payload)
    print("Test case 5 (Invalid Cookie):", response.status_code, response.text)


def invalid_http_method():
    payload = json.dumps({
        "phone_or_email": "09104491104"
    })
    response = requests.get(url, headers=headers, data=payload)  # Using GET instead of POST
    print("Test case 6 (Invalid HTTP method):", response.status_code, response.text)


def large_payload():
    payload = json.dumps({
        "phone_or_email": "09104491104" * 1000  # Simulate a very large phone number field
    })
    response = requests.post(url, headers=headers, data=payload)
    print("Test case 7 (Large payload size):", response.status_code, response.text)


def malformed_json():
    payload = '{"phone_or_email": "09104491104" '  # Malformed JSON (missing closing bracket)
    response = requests.post(url, headers=headers, data=payload)
    print("Test case 8 (Malformed JSON):", response.status_code, response.text)


def server_not_reachable():
    url_invalid = "https://api-staging.invalidurl.com/register/"  # Invalid URL to simulate server not reachable
    payload = json.dumps({
        "phone_or_email": "09104491104"
    })

    try:
        response = requests.post(url_invalid, headers=headers, data=payload)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.exceptions.RequestException as e:
        print(f"Test case 9 (Server not reachable): {e}")
        print("خطا: سرور در دسترس نیست. لطفاً URL یا اتصال شبکه خود را بررسی کنید.")



def server_error():
    payload = json.dumps({
        "phone_or_email": "09104491104"
    })
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code != 200:
        print("Test case 10 (Server error):", response.status_code, response.text)

def xss_injection():
    xss_input = "<script>alert('XSS')</script>"
    payload = json.dumps({
        "phone_or_email": "09104491104",
        "username": xss_input,
        "password": "testpassword"
    })
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        print(f"Test failed. XSS input '{xss_input}' should have been blocked.")
    else:
        print(f"Test case 11 (Error caught as expected for XSS injection): {response.status_code} - {response.text}")

def sql_injection():
    url = "YOUR_REGISTRATION_ENDPOINT_HERE"
    headers = {'Content-Type': 'application/json'}
    sql_injection_input = "' OR '1'='1"
    payload = json.dumps({
        "username": sql_injection_input,
        "password": "some_password"
    })

    try:
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:  # Or whatever success code is expected
            print(f"Test failed. SQL Injection input '{sql_injection_input}' was not blocked. Status Code: {response.status_code}, Response: {response.text}")
        else:
            print(f"Test passed (potentially). SQL Injection attempt resulted in status code: {response.status_code}, Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Test case 12 (Error during request): {e}")

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
        print(f"Test case 13 (Error caught as expected for CSRF attack): {response.status_code} - {response.text}")


def run_negative_register_tests():

    missing_phone_or_email()
    invalid_phone_format()
    invalid_email_format()
    empty_phone_or_email()

    invalid_cookie()
    invalid_http_method()

    large_payload()
    malformed_json()
    server_not_reachable()

    server_error()
    xss_injection()
    sql_injection()

run_negative_register_tests()
