from django.urls import path, include

app_name = 'core'

urlpatterns = [
    path('project/', include('hextrack.components.core.controllers.project.urls')),
]
