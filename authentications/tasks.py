from django.core.mail import EmailMessage
from django.conf import settings
from conf.celery import app


@app.task()
def send_email(data):
    # Ensure the email body is a string
    email = EmailMessage(
        subject=data["email_subject"],
        body=data["email_body"],
        to=data["to_email"],
        from_email=settings.EMAIL_HOST_USER,
    )
    email.content_subtype = "html"
    email.send()
