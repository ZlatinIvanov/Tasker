from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasker.accounts'

    def ready(self):
        import tasker.accounts.signals