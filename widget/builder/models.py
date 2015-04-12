import uuid

from django.db import models

from postgres.fields import json_field


class DeclarationStore(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False)
    declaration_url = models.URLField()
    declaration_id = models.IntegerField()
    declaration_data = json_field.JSONField(default={})
    generated_image = models.URLField(blank=True, null=True)
