from django.urls import path

from . import controllers

urlpatterns = [
    path('', controllers.ProjectGetAllController.as_view(), name='project.all'),
    path('<int:id>', controllers.ProjectGetController.as_view(), name='project.get'),
    path('<int:id>/update', controllers.ProjectUpdateController.as_view(), name='project.update'),
    path('<int:id>/archive', controllers.ProjectArchiveController.as_view(), name='project.archive'),
    path('<int:id>/delete', controllers.ProjectDeleteController.as_view(), name='project.delete'),
    path('create', controllers.ProjectCreateController.as_view(), name='project.create'),
]
