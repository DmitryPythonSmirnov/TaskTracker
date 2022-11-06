from django.core.management.base import BaseCommand
from authapp.models import DiaryUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        DiaryUser.objects.create_superuser(username='django', password='superuser12#')
