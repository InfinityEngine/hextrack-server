import hexdi
from api_commons.common import ApiResponse
from hextrack.commons.controllers import HextrackController
from hextrack.commons.decorators import inject_dto
from hextrack.components.core.services import ProjectService
from hextrack.components.core.dto import ProjectDto, ProjectOutDto


class ProjectGetAllController(HextrackController):

    @property
    @hexdi.dependency(ProjectService)
    def service(self) -> ProjectService: pass

    def get(self, request):
        archived = request.GET.get('archived') in [1, "true", True]
        projects = self.service.get_all(archived=archived)
        project_dtos = list([ProjectOutDto.from_model(project) for project in projects])
        return ApiResponse.success(project_dtos)


class ProjectGetController(HextrackController):
    @property
    @hexdi.dependency(ProjectService)
    def service(self) -> ProjectService: pass

    def get(self, request, pk: int):
        project = self.service.get(pk=pk)
        project_dto = ProjectOutDto.from_model(project)
        return ApiResponse.success(project_dto)


class ProjectCreateController(HextrackController):
    @property
    @hexdi.dependency(ProjectService)
    def service(self) -> ProjectService: pass

    @inject_dto(ProjectDto)
    def post(self, request, dto: ProjectDto):
        project = self.service.create(dto.name)
        project_dto = ProjectOutDto.from_model(project)
        return ApiResponse.success(project_dto)


class ProjectUpdateController(HextrackController):
    @property
    @hexdi.dependency(ProjectService)
    def service(self) -> ProjectService: pass

    @inject_dto(ProjectDto)
    def put(self, request, pk: int, dto: ProjectDto):
        project = self.service.update(pk, dto.name)
        project_dto = ProjectOutDto.from_model(project)
        return ApiResponse.success(project_dto)


class ProjectArchiveController(HextrackController):
    @property
    @hexdi.dependency(ProjectService)
    def service(self) -> ProjectService: pass

    def put(self, request, pk: int):
        self.service.toggle_archive(pk, archive=True)
        return ApiResponse.success()


class ProjectRestoreController(HextrackController):
    @property
    @hexdi.dependency(ProjectService)
    def service(self) -> ProjectService: pass

    def put(self, request, pk: int):
        self.service.toggle_archive(pk, archive=False)
        return ApiResponse.success()


class ProjectDeleteController(HextrackController):
    @property
    @hexdi.dependency(ProjectService)
    def service(self) -> ProjectService: pass

    def delete(self, request, pk: int):
        self.service.soft_delete(pk)
        return ApiResponse.success()
