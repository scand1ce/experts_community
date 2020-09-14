import factory
from django.utils.timezone import now
from posts import models
from users.tests.users_factories import UserFactory


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Post

    author = factory.SubFactory(UserFactory)
    title = factory.Sequence(lambda n: 'TEST_title%s' % n)
    created_at = factory.LazyAttribute(lambda x: now())
    is_published = True
    content = factory.Faker('paragraph')  # factory.Sequence(lambda n: 'TEST_content%s' % n)
    photo = factory.django.ImageField(color='blue')





# from posts.tests.posts_factories import *
# post = PostFactory()