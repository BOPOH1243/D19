from django.dispatch import receiver
from .models import Response
from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from django.conf import settings



@receiver(post_save, sender=Response)
def post_save_response(instance, **kwargs):
    response = instance
    user = instance.user
    post_author = instance.post.author
    post = instance.post
    print(f'отклик создан, пост:{instance.post}, пользователь:{instance.user}, текст:{instance.text}')

    '''html_content = render_to_string(
        'mail/schedule_news.html',
        {
            'news': posts,
        }
    )'''
    msg = EmailMultiAlternatives(
        subject=f'отклик на пост {post.header}',
        body=f'дорогой {user}, ты откликнулся на пост {post}',  # это то же, что и message
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email],  # это то же, что и recipients_list
    )
    #msg.attach_alternative(html_content, "text/html")  # добавляем html
    try:
        msg.send()
    except:
        print(f'{msg} ошибка отправки')

    msg = EmailMultiAlternatives(
        subject=f'отклик на пост {post.header}',
        body=f'дорогой {post_author}, на твой пост ({post}) откликнулся {user} сообщением:\n{instance.text}',  # это то же, что и message
        from_email=settings.EMAIL_HOST_USER,
        to=[post_author.email],  # это то же, что и recipients_list
    )
    try:
        msg.send()
    except:
        print(f'{msg} ошибка отправки')


