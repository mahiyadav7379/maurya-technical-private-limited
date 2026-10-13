import urllib.request
import urllib.parse
import json
from django.conf import settings

def verify_recaptcha(request):
    """
    Verifies Google reCAPTCHA v2 token sent via POST request ('g-recaptcha-response').
    Returns True if valid or in development test key mode, False otherwise.
    """
    recaptcha_response = request.POST.get('g-recaptcha-response')
    secret_key = getattr(settings, 'RECAPTCHA_SECRET_KEY', '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe')

    if not recaptcha_response:
        return False

    try:
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': secret_key,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode('utf-8')
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req, timeout=5)
        result = json.loads(response.read().decode('utf-8'))

        if result.get('success'):
            return True
        elif secret_key == '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe':
            # Support development test key fallback
            return True
    except Exception:
        # Network error or offline environment fallback for default dev key
        if secret_key == '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe':
            return True

    return False


def validate_indian_phone(phone_str):
    """
    Validates Indian 10-digit mobile number.
    Rejects dummy, fake, repetitive, or invalid numbers.
    Returns (is_valid: bool, result: str)
    """
    import re

    if not phone_str or not str(phone_str).strip():
        return False, "Mobile number is required."
    
    # Strip spaces, dashes, brackets, and non-digit characters
    digits = re.sub(r'\D', '', str(phone_str))

    # Strip country code 91 if 12 digits
    if len(digits) == 12 and digits.startswith('91'):
        digits = digits[2:]
    # Strip leading 0 if 11 digits
    elif len(digits) == 11 and digits.startswith('0'):
        digits = digits[1:]

    # Check length
    if len(digits) != 10:
        return False, "Please enter a valid 10-digit mobile number."

    # Check Indian mobile number starting prefix (6, 7, 8, 9)
    if digits[0] not in ['6', '7', '8', '9']:
        return False, "Mobile number must start with 6, 7, 8, or 9."

    unique_digits = set(digits)

    # Reject all same digit (e.g. 0000000000, 1111111111, 9999999999)
    if len(unique_digits) == 1:
        return False, "Dummy phone number (e.g. 9999999999) is not allowed."

    # Reject dummy sequential numbers
    dummy_sequences = {
        '1234567890', '0123456789', '9876543210', '0987654321', 
        '2345678901', '3456789012', '4567890123', '9012345678'
    }
    if digits in dummy_sequences:
        return False, "Dummy sequence phone number is not allowed."

    # Reject repetitive digit flooding (e.g. 9000000000, 8000000000, 9999900000)
    for ch in unique_digits:
        if digits.count(ch) >= 7:
            return False, "Dummy phone number (e.g. 9000000000) detected. Please enter a valid mobile number."

    # Reject repeating 2-digit or 3-digit patterns (e.g. 9898989898, 1212121212)
    if digits[:2] * 5 == digits or (digits[:3] * 3 + digits[0]) == digits:
        return False, "Repetitive dummy phone pattern is not allowed."

    return True, digits

