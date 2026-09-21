from django.conf import settings

def recaptcha_context(request):
    return {
        'recaptcha_site_key': getattr(settings, 'RECAPTCHA_SITE_KEY', '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI')
    }
