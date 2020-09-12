import factory
from users import models



class UserFactory(factory.Factory):
    class Meta:
        model = models.CustomUser

    username = factory.Sequence(lambda n: 'TEST_username%s' % n)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = 'email@email.email'
    is_superuser = True
    is_active = True
    is_staff = True
    password = factory.PostGenerationMethodCall('set_password', 'defaultpassword')


'''
pipenv shell

python manage.py shell_plus

from users.tests.factories import *

UserFactory().save()
'''
