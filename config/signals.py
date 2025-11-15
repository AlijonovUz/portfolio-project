from django.db.models.signals import post_migrate
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.dispatch import receiver

from .models import Data


@receiver(post_migrate)
def create_default_data(sender, **kwargs):
    try:
        if not Data.objects.exists():
            fake_cv = ContentFile(b"Default CV content", name="default_cv.txt")
            Data.objects.create(
                cv=fake_cv,
                address="Farg‘ona shahri, O‘zbekiston",
                email="admin@example.com",
                phone="+998901234567",
            )
            print("Data qo'shildi.")
    except Exception:
        pass


@receiver(post_migrate)
def create_default_admin(sender, **kwargs):
    try:
        if not User.objects.exists():
            User.objects.create_user(
                username="admin",
                email="admin@example.com",
                password="admin",
                is_superuser=True,
                is_staff=True
            )
            print("Admin qo'shildi.")
    except Exception:
        pass
