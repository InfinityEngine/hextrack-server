import abc
import typing
import hextrack.components.core.models.project as project


class ProjectService:
    @abc.abstractmethod
    def get_all(self, archived=False) -> typing.List[project.Project]: pass

    @abc.abstractmethod
    def get(self, pk) -> project.Project: pass

    @abc.abstractmethod
    def create(self, name) -> project.Project: pass

    @abc.abstractmethod
    def update(self, pk, name) -> project.Project: pass

    @abc.abstractmethod
    def toggle_archive(self, pk, archive) -> None: pass

    @abc.abstractmethod
    def soft_delete(self, pk) -> None: pass
