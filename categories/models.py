from django.db import models

from common.models import UUIDModel


class Category(UUIDModel):
    name = models.CharField(
        max_length=100,
        db_column='name'
    )
    color = models.CharField(
        max_length=7,
        db_column='color'
    )

    class Meta:
        db_table = 'categories'
