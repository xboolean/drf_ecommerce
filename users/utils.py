from django.core.mail import EmailMessage
from rest_framework.response import Response

def send_email(data):
    is_ok = EmailMessage(subject=data['mail_subject'], body=data['mail_body'], to=[data['to_email']]).send()
    if not is_ok:
        return Response(data={'error': 'Face somer error while trying to send token to your email. Please try later.'})