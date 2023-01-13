from django.db import models
from datetime import date
from django.utils.translation import gettext as _
# Create your models here.


class Energy_consumption(models.Model):
    user_id = models.CharField(max_length=20, null=True)
    user_name = models.CharField(max_length=20, null=True)
    house_number = models.CharField(max_length=200, null=True)
    date_used = models.DateField(_("Date"), default=date.today)
    consume = models.CharField(max_length=200, null=True)
