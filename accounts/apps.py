from django.apps import AppConfig
from django.db.models.signals import post_migrate
from accounts import handlers

class MyAppConfig(AppConfig):
    name = 'accounts'
    verbose_name = 'My Accounts'

    def ready(self):
        post_migrate.connect(handlers.create_notice_types, sender=self)
