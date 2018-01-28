from django.urls import path

from . import controllers

urlpatterns = [
    path('', controllers.ProjectGetAllController.as_view(), name='project.all'),
    path('<int:pk>', controllers.ProjectGetController.as_view(), name='project.get'),
    path('<int:pk>/update', controllers.ProjectUpdateController.as_view(), name='project.update'),
    path('<int:pk>/archive', controllers.ProjectArchiveController.as_view(), name='project.archive'),
    path('<int:pk>/restore', controllers.ProjectRestoreController.as_view(), name='project.restore'),
    path('<int:pk>/delete', controllers.ProjectDeleteController.as_view(), name='project.delete'),
    path('create', controllers.ProjectCreateController.as_view(), name='project.create'),
]
