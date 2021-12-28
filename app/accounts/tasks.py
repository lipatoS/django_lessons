from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def activate_email(activation_link,email_to):
    subject = "Активируй свою почту"
    body = f'''
    привет
    твоя ссылка для активации брат
    {activation_link}
    '''
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [email_to],
        fail_silently=False,
    )
