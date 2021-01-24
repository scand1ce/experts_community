from django import template
from ..models import Post
from experts_community.settings import BOT_TOKEN, CHAT_ID

register = template.Library()


@register.simple_tag
def send_request_for_bot():
    import requests
    post = Post.objects.all().first()
    request_body = requests.get(
            f'https://api.telegram.org/bot{BOT_TOKEN}/' \
            f'sendMessage?chat_id={CHAT_ID}' \
            f'&text=Опубликован новый пост: {post.title}\n' \
            f'Автор: {post.author}\n'
            f'Опубликовано: {post.created_at}'
    )

    return request_body
