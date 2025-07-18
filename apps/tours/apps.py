from django.apps import AppConfig


class ToursConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.tours'

    def ready(self):
        import apps.tours.signals
