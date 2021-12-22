from django.urls import include, path
from accounts.views import MyProfileView
from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'
urlpatterns = [

    path('my-profile/<int:pk>', MyProfileView.as_view(), name="my-profile"),
    path('change-password/<int:pk>',
         auth_views.PasswordChangeView.as_view(
             template_name="password_change.html",
             success_url='/'  # не могу поставить другую ссылку :(
         ),
         name="change-password"),
    # path('password_reset/<int:pk>', auth_views.PasswordResetView(), name='password_reset')

]
