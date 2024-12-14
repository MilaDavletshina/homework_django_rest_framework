from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from celery import shared_task

from materials.models import Subscription


@shared_task
def send_information_about_course_update(course_id):
    """Отправляет сообщение пльзователю о подписке."""
    subject = "Обновление курса!"
    message = "Информируем Вас о том, что материалы курса обновлены!"
    subscription = Subscription.objects.filter(course_id=course_id)
    for s in subscription:
        send_mail(subject, message, EMAIL_HOST_USER, [s.user.email])

