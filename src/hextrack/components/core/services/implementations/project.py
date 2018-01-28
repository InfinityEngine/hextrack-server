import hexdi
import typing
from django.db import IntegrityError
from hextrack.commons import errors
from hextrack.components.core.models import project
from hextrack.components.core.services import ProjectService


@hexdi.permanent(ProjectService)
class ProjectServiceImpl(ProjectService):
    def _get_queryset(self):
        return project.Project.objects.filter(soft_deleted=False)

    def get_all(self, archived=False) -> typing.List[project.Project]:
        try:
            return list(self._get_queryset().filter(archived=archived).all())
        except Exception:
            raise errors.UnexpectedError

    def get(self, pk) -> project.Project:
        try:
            return self._get_queryset().get(pk=pk)
        except project.Project.DoesNotExist:
            raise errors.NotFoundError(project.Project, pk=pk)

    def create(self, name) -> project.Project:
        try:
            return project.Project.objects.create(name=name)
        except IntegrityError:
            raise errors.NotUniqueError(project.Project, fields={'name': name})

    def update(self, pk, name) -> project.Project:
        proj = self.get(pk)
        try:
            proj.name = name
            proj.save()
            return proj
        except IntegrityError:
            raise errors.NotUniqueError(project.Project, fields={'pk': pk, 'name': name})

    def toggle_archive(self, pk, archive) -> None:
        proj = self.get(pk)
        try:
            proj.archived = archive
            proj.save()
        except Exception:
            raise errors.UnexpectedError

    def soft_delete(self, pk) -> None:
        proj = self.get(pk)
        try:
            proj.soft_deleted = True
            proj.save()
        except Exception:
            raise errors.UnexpectedError
