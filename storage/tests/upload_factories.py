import factory
from storage import models
from faker import Factory
from users.tests.users_factories import UserFactory
import random

x = random.uniform(720.00, 20000.00)
fake = Factory.create()


class UploadFileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.UploadFilesModel

    number = factory.Sequence(lambda n: n)
    title = fake.sentence(nb_words=2)
    comment = fake.text()
    file = factory.django.FileField(filename='the_file.dat')
    sum = x
    uploader = factory.SubFactory(UserFactory)
