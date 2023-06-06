import os

from django.core.mail import send_mail


def send_activation_link(email, activation_code):
    full_link = f'http://{os.environ.get("HOST")}:{os.environ.get("PORT")}/api/v1/account/activate/{activation_code}'
    send_mail(
        'Ссылка активации',
        full_link,
        os.environ.get("EMAIL_HOST_USER"),
        [email]
    )


def send_activation_code(email, activation_code):
    send_mail(
        'Пароль активации',
        activation_code,
        os.environ.get("EMAIL_HOST_USER"),
        [email],
    )


def send_register_link(email):
    full_link = f'http://{os.environ.get("HOST")}:{os.environ.get("PORT")}/api/v1/account/register/'
    send_mail(
        'Ссылка регистрации',
        full_link,
        os.environ.get("EMAIL_HOST_USER"),
        [email]
    )
