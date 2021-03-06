from django.db.models import Max
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import User


@receiver(pre_save, sender=User)
def create_account_no(sender, instance, *args, **kwargs):
    if not instance.account_no:

        largest = User.objects.all().aggregate(
            Max("account_no")
            )['account_no__max']

        if largest:

            instance.account_no = largest + 1
        else:

            instance.account_no = 10000000
