from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, View, RedirectView
from django.views.generic import ListView
# Create your views here.
from accounts.models import User
from accounts.forms import SingUpForms
from django.views.generic import TemplateView
from django.contrib import messages


class PassSuccssesViews(TemplateView):
    template_name = "password_success.html"


class MyProfileView(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    fields = ('first_name', 'last_name')
    success_url = reverse_lazy("index")
    template_name = "my_profile.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.request.user.id)
        return queryset


class SingUpView(CreateView):
    model = User
    template_name = "sing_up.html"
    form_class = SingUpForms
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        messages.info(self.request, "зарегенился, а теперь сходи на почту")
        return super().form_valid(form)


class ActivateView(RedirectView):
    pattern_name = "index"

    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.pop("username")
        print(f"-----------------------------------username = {username}")

        user = get_object_or_404(User, username=username, is_active=False)
        user.is_active = True
        user.save(update_fields=('is_active',))
        messages.info(self.request, 'активироватовл ирывпяилияывачполиоваыиатвычптвч')

        return super().get_redirect_url(*args, **kwargs)
