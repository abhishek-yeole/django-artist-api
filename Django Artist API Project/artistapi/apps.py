from django.apps import AppConfig

class ArtistapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'artistapi'

    def ready(self):
        import artistapi.signals
