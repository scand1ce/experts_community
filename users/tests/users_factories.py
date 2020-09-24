import factory
from users import models
from faker import Factory

fake = Factory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.CustomUser

    avatar = factory.django.ImageField(color='red')
    username = factory.Sequence(lambda n: 'username%s' % n)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = fake.email()  # 'ascii_company_email' -->
    # AttributeError: 'Generator' object has no attribute 'ascii_company_email'
    department = factory.Sequence(lambda n: 'NTE%s' % n)
    is_superuser = False
    is_active = True
    is_staff = False
    password = factory.PostGenerationMethodCall('set_password', 'defaultpassword')