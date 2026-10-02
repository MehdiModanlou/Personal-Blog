from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


class UserProfileView(DetailView):
    model = CustomUser
    template_name = "accounts/profile_view.html"
    slug_field = "username"
    slug_url_kwarg = "username"

