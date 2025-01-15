from celery import shared_task
from celery.result import AsyncResult
from django.core.mail import send_mail
import time

from store.models import Product

@shared_task
def add(x, y):
    """
    Тестовая задача для проверки связки Celery+Redis
    """
    time.sleep(5)
    return x + y


@shared_task
def send_notification_email(subject, message, recipient_list):
    """
    Задание по отправки уведомлений на почту
    """
    time.sleep(5)
    send_mail(
        subject = subject,
        message = message,
        from_email = 'skoch2000@yandex.ru',
        recipient_list = [recipient_list],
    )
    return f'Email sent to {recipient_list}'


@shared_task
def check_task_status(task_id):
    """
    Задание для отслеживания статуса выполнения задания
    """
    result = AsyncResult(task_id)
    return {
        'task_id': task_id,
        'status': result.status,
        'result': result.result,
    }


@shared_task
def update_product_price():
    """
    Периодическое задание по увеличению цены на 5%
    """
    products = Product.objects.all()
    for product in products:
        product.price = product.price * 1.05
        product.save()
    return f'Цена обновлена для {products.count()} продуктов'
