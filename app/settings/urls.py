from django.contrib import admin
from django.urls import path
from currency.views import response_codes
from currency.views import IndexViews
from currency.views import GenPassViews
from currency.views import ContactUsViews
# from django.contrib.auth.urls
import debug_toolbar
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('', IndexViews.as_view(), name="index"),
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('gen/', GenPassViews.as_view()),
    path('response/', response_codes),
    path("currency/", include("currency.urls")),
    path('contact_us_create/', ContactUsViews.as_view(), name="contact_us_create"),
    path('auth/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls'))


]
