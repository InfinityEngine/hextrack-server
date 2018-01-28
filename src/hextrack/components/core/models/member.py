from hextrack.commons.utils import ChoiceEnum
from django.conf import settings
from django.db import models
from .common import AuditableModel


class MemberType(ChoiceEnum):
    ADMIN = "Admin"
    MANAGER = "Manager"
    DEVELOPER = "Developer"
    QA = "QA"
    CLIENT = "Client"


class ProjectMember(AuditableModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='members', null=False, blank=False)
    member_type = models.CharField(max_length=255, null=False, blank=False, choices=MemberType.choices())
