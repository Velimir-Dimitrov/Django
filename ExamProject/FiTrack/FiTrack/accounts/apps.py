from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FiTrack.accounts'

    def ready(self):
        import FiTrack.accounts.signals