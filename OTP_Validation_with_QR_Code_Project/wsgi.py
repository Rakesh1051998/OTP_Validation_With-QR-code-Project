"""
WSGI config for OTP_Validation_with_QR_Code_Project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OTP_Validation_with_QR_Code_Project.settings')

application = get_wsgi_application()
