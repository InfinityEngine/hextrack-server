from django.db import models
from django.conf import settings


class AuditableModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name="%(class)s_creators",
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name="%(class)s_updaters",
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True)

    class Meta:
        abstract = True
