from django.core.management.base import BaseCommand
from store.models import Category

class Command(BaseCommand):
    help = 'Delete all categories and products from database'

    def handle(self, *args, **options):
        Category.objects.all().delete()
