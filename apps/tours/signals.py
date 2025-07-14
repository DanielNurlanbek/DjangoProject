from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.tours.models import Review
from apps.tours.utils import send_tg_message
from core import settings


@receiver(post_save, sender=Review)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = "Спасибо за ваш отзыв!"
        message = f"Здравствуйте, {instance.fio}!\nСпасибо за ваш отзыв и оценку."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]
        send_mail(subject, message, email_from, recipient_list)


@receiver(post_save, sender=Review)
def send_user_register(sender, instance, created, **kwargs):
    if created:
        text = f"Новый отзыв:\nФИО: {instance.fio}\nEmail: {instance.email}\nОценка: {instance.rating}"
        send_tg_message(text)