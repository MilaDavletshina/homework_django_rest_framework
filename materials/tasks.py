from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_information_about_course_update(email):
    """Отправляет сообщение пльзователю о подписке."""
    subject = "Обновление курса!"
    message = "Информируем Вас о том, что материалы курса обновлены!"

    send_mail(subject, message, EMAIL_HOST_USER, [email])

