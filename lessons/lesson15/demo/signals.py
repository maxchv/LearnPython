from datetime import datetime

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal

from demo.models import Teacher

email_receive = Signal()


@receiver(email_receive)
def email_receive_handler(sender, **kwargs):
    print("Email receive first from", kwargs.get('email'))
    raise Exception


@receiver(email_receive)
def email_receive_handler2(sender, **kwargs):
    print("Email receive second from", kwargs.get('email'))


def request_start_handler(sender, **kwargs):
    print('Request started at', datetime.now())


# @receiver(request_finished)
# def request_finished_handler(sender, **kwargs):
#     print('Request finished at', datetime.now())


@receiver(post_save, sender=User)
def user_save_handler(sender, **kwargs):
    user = kwargs.get('instance')
    Teacher.objects.create(user=user)
    print("Save user", user)
