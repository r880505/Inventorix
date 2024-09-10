from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView, LogoutView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<uuid:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('logout/', LogoutView.as_view(), name='logout'),
]