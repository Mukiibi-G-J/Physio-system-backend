from django.core.mail import send_mail
import random
from django.template.loader import render_to_string
from authentication.models import CustomUser as User
import pathlib

# location of email_verif.html
BASE_DIR = pathlib.Path(__file__).parent.parent


def send_email_verification(email, user):
    subject = "Verify your email"
    otp = random.randint(10000, 99999)
    message = f"Hi {user.username}, your OTP is {otp}"
    html_content = render_to_string(
        "email_verif.html", {"otp": otp, "username": user.username}
    )

    # Send the email
    send_mail(
        subject,
        message,
        'kalideveloper865@gmail.com',
        # from email and to email
        [email],
        html_message=html_content,
    )
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()