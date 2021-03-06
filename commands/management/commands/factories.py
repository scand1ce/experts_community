from django.core.management.base import BaseCommand
from posts.tests.comment_factories import CommentFactory
from posts.tests.posts_factories import PostFactory
from storage.tests.upload_factories import UploadFileFactory
from users.tests.users_factories import UserFactory
from posts.models import Post


class Command(BaseCommand):

    def handle(self, *args, **options):
        user1 = UserFactory.create()
        user2 = UserFactory.create()
        PostFactory.create_batch(2, author=user1)
        for post in Post.objects.filter(author=user1):
            CommentFactory.create_batch(5, author=user2, post=post)

            UploadFileFactory.create_batch(5, uploader=user1)
            UploadFileFactory.create_batch(5, uploader=user2)

