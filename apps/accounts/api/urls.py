from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'accounts'

urlpatterns = [
    path('auth/', views.auth),
]

urlpatterns = format_suffix_patterns(urlpatterns)
