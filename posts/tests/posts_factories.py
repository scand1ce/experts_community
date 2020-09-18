import datetime
import factory
from faker import Factory
from posts import models
from users.tests.users_factories import UserFactory
fake = Factory.create()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Post

    author = factory.SubFactory(UserFactory)
    title = fake.sentence(nb_words=3)
    created_at = factory.LazyFunction(datetime.datetime.now)
    is_published = True
    content = fake.text()
    photo = factory.django.ImageField(color='blue')
