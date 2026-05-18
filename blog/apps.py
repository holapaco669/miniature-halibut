from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"

    def ready(self):
        from django.contrib.sessions.models import Session
        try:
            Session.objects.all().delete()
        except:
            pass