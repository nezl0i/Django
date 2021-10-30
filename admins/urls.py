from django.urls import path

from admins.views import AdminIndexTemplate, UserListView, UserCreateView, UserUpdateView, UserDeleteView

app_name = 'baskets'

urlpatterns = [
    path('', AdminIndexTemplate.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),
]
