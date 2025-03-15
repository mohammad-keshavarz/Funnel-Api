import json
import requests

def send_otp_request(cell_phone, request_type):
    url = f"https://api-staging.tabdealbot.com/utils/staging/otp/?cell_phone={cell_phone}&type={request_type}"

    payload = json.dumps({
        "phone_or_email": cell_phone
    })

    headers = {
        'cell_phone': cell_phone,
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

# مثال استفاده از تابع
result = send_otp_request(cell_phone="09102222222", request_type="Registration")