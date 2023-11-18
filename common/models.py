from uuid import uuid4
from django.db import models


class UUIDModel(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        db_column='uuid'
    )
    creation_date = models.DateTimeField(
        auto_now_add=True,
        null=True,
        db_column='creation_date'
    )
