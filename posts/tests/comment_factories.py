import factory
from django.utils.timezone import now
from posts import models
from posts.tests.posts_factories import PostFactory
from users.tests.users_factories import UserFactory


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Comment

    author = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    created_at = factory.LazyAttribute(lambda x: now())
    comment_text = factory.Faker('paragraph')
