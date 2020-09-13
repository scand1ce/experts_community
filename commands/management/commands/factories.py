from django.core.management.base import BaseCommand

from posts.tests.comment_factories import CommentFactory


class Command(BaseCommand):
    #  handle обязательный метод класса Command, без него выдает ошибку, хотя создает все с помощью фабрик
    def handle(self, *args, **options):
        CommentFactory.create_batch(10)
