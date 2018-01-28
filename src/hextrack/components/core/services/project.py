import hextrack.components.core.models.project as project


class ProjectService:
    def get(self, pk) -> project.Project: pass

    def create(self, name) -> project.Project: pass

    def update(self, pk, name) -> None: pass

    def archive(self, pk) -> None: pass

    def delete(self, pk) -> None: pass
