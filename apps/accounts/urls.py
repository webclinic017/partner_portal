from django.contrib.auth.views import LoginView, logout_then_login
from django.urls import include, path
from .views import *
from .api import urls as routers
# from .api.urls import urlpatterns as router


app_name = 'accounts'

urlpatterns = [
    # login e logou
    path('accounts/login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/logout/', logout_then_login, name='logout'),
    # api - login na oxentetv
    path('accounts/api-technobox/', include(routers)),
    # profile
    path('profile/', ProfileView.as_view(), name='profile'),
    path('monitor-network/', MonitorNetworkDashboardView.as_view(), name='monitor_network_dashboard'),
    path('monitor-network/<int:pk>/detail/', MonitorNetworkDetailView.as_view(), name='monitor_network_detail'),
    path('customer-user/', CustomerUserListView.as_view(), name='customeruser_list'),
    path('customer-user/create/', CustomerUserCreateView.as_view(), name='customeruser_create'),
    path('customer-user/<int:pk>/update/', CustomerUserUpdateView.as_view(), name='customeruser_update'),
    path('customer-user/<int:pk>/delete/', CustomerUserDeleteView.as_view(), name='customeruser_delete'),
    path('customer-user/<int:pk>/change-status/', CustomerUserChangeStatusView.as_view(), name="customeruser_change_status"),
    path('customer-user/update-password/', CustomerUserUpdatePassword.as_view(), name='customeruser_update_password'),
]
