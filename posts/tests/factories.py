import factory
from django.utils.timezone import now
from posts import models
from users.tests.factories import UserFactory


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Post

    author = factory.SubFactory(UserFactory)
    title = factory.Sequence(lambda n: 'TEST_title%s' % n)
    created_at = factory.LazyAttribute(lambda x: now())
    is_published = True
    content = factory.Sequence(lambda n: 'TEST_content%s' % n)
    photo = factory.django.ImageField(color='blue')






'''
pipenv shell

python manage.py shell_plus

from posts.tests.factories import *

# Builds and saves a User and a Post

>>> post = PostFactory()

>>> post.id is None  # Post has been 'saved'
False

>>> post.author.id is None  # post.author has been saved
False

'''