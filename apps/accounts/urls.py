from django.urls import include, path
from . import views
from .api import urls as routers
# from .api.urls import urlpatterns as router


app_name = 'accounts'

urlpatterns = [
    path('api-technobox/', include(routers)),
]
