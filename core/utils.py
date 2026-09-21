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
