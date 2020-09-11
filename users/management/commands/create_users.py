from users.models import CustomUser
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = u'Создание случайного пользователя'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Количество создаваемых пользователей')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            CustomUser.objects.create_user(
                department='TEST',
                first_name=get_random_string(),
                last_name=get_random_string(),
                is_superuser=False,
                is_active=True,
                username=get_random_string(),
                email=get_random_string(),
                password='12345678FF')
