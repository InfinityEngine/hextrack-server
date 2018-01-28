from django.db import models
from .common import AuditableModel


class Project(AuditableModel):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    archived = models.BooleanField(null=False, blank=False, default=False)
    soft_deleted = models.BooleanField(null=False, blank=False, default=False)
