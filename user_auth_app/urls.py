from django.urls import path
from .views import (
    UserList, UserDetails, GroupList
)

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),
]
