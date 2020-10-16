from django.core.management.base import BaseCommand
from users.models import CustomUser

'''Команда для проверки последнего входа в систему 
пользователя "testuser" который создан для 
демонстративных целей

'''


class Command(BaseCommand):
    def handle(self, *args, **options):

        users = CustomUser.objects.all()

        for u in users:
            if u.username == 'testuser':
                print(
                    '\n------------------\n',
                    u.username,
                    '\t', '||',
                    u.last_login,
                    '\n------------------\n',
                )
