from django.urls import path

from .views import SignUpView, UserProfileView

app_name = "accounts"


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("userprofile/<str:username>/", 
         UserProfileView.as_view(), 
         name="userprofile")
]
