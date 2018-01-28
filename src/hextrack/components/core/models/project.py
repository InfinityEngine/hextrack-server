from django.db import models
from .common import AuditableModel


class Project(AuditableModel):
    name = models.CharField(max_length=255, null=False, blank=False)

