from django.contrib.auth.views import LoginView, logout_then_login
from django.urls import include, path
from .views import ProfileView
from .api import urls as routers
# from .api.urls import urlpatterns as router


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', logout_then_login, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('api-technobox/', include(routers)),
]
