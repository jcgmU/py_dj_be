from django.apps import AppConfig


class DjangoAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "infrastructure.django_app"  # Cambiado para coincidir con la estructura
