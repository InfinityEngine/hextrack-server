from api_commons.common import error_404_handler, error_500_handler
from django.urls import path, include

app_name = 'core'

urlpatterns = [
    path('project/', include('hextrack.components.core.controllers.project.urls')),
]

handler404 = error_404_handler
handler500 = error_500_handler
