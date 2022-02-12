from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Cuenta


@receiver(post_save, sender=User)
def crear_cuenta(sender, instance, created, **kwargs):
    if created:
        Cuenta.objects.create(user=instance)


@receiver(post_save, sender=User)
def guardar_cuenta(sender, instance, **kwargs):
        instance.cuenta.save()