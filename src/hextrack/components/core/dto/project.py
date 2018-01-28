from hextrack.components.core.models import Project
from rest_framework import fields
from api_commons.dto import BaseDto


class ProjectDto(BaseDto):
    name = fields.CharField(max_length=255, required=True)
    archived = fields.BooleanField(required=False)

    @classmethod
    def from_model(cls, model: Project):
        dto = cls()
        dto.name = model.name
        dto.archived = model.archived
        return dto


class ProjectOutDto(ProjectDto):
    id = fields.IntegerField(required=True)

    @classmethod
    def from_model(cls, model: Project):
        dto = cls()
        dto.name = model.name
        dto.archived = model.archived
        dto.id = model.pk
        return dto
