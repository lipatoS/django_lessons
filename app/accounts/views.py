from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import ListView
# Create your views here.
from accounts.models import User


class MyProfileView(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    fields = ('first_name', 'last_name')
    success_url = reverse_lazy("index")
    template_name = "my_profile.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.request.user.id)
        return queryset


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordsChangeForm
    # success_url = reverse_lazy('')


class PasswordSuccess(ListView):
    template_name = "registration/password_success.html"
