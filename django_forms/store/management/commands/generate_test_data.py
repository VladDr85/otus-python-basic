from store.models import Category, Product
from django.core.management.base import BaseCommand
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Generates fake data'
    def handle(self, *args, **options):

        self.stdout.write("Запоминаем категории...")
        category_list = []
        category_list = Category.objects.all()
        if category_list:
            self.stdout.write(f"Существуют категории: {category_list}")

            self.stdout.write("Начинаем генерацию Данных...")
            fake = Faker()
            for _ in range(10):
                product_name = fake.sentence(nb_words=6)
                product_description = fake.text(max_nb_chars=100)
                product_price = fake.port_number()
                product_created_at = fake.date_time_this_year()
                product_category = random.choice(category_list)

                product = Product.objects.create(
                    name=product_name,
                    description=product_description,
                    price=product_price,
                    created_at=product_created_at,
                    category=product_category
                )
            self.stdout.write("Создали 10 товаров!")
        else:
            self.stdout.write(f"Создание товаров не возможно. Отсутствуют категории!")
