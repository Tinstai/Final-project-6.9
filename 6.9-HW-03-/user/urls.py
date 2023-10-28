from django.urls import path
from user.views import (
    UserProfileView
)

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile')
]
