"""
WSGI config for maurya_technical project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from pathlib import Path
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maurya_technical.settings')

application = get_wsgi_application()

base_dir = Path(__file__).resolve().parent.parent
staticfiles_dir = base_dir / 'staticfiles'
static_dir = base_dir / 'static'

if staticfiles_dir.exists():
    application = WhiteNoise(application, root=str(staticfiles_dir), prefix='static/')
    if static_dir.exists():
        application.add_files(str(static_dir), prefix='static/')
elif static_dir.exists():
    application = WhiteNoise(application, root=str(static_dir), prefix='static/')

# For Vercel serverless function
app = application

