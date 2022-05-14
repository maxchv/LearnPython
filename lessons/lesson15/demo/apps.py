from django.apps import AppConfig
from django.core.signals import request_started


class DemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'demo'

    def ready(self):
        from . import signals  # регистрация всех слушателей с декоратором @receiver
        # request_started.connect(signals.request_start_handler)
