from django.contrib import admin
from django.urls import path
from currency.views import RateCreateViews
from currency.views import Rate2CreateViews
from currency.views import Rate2ListViews
from currency.views import RateListViews
from currency.views import KursListViews
from currency.views import RateUpdateViews
from currency.views import Rate2UpdateViews
from currency.views import RateDetailViews
from currency.views import Rate2DetailViews
from currency.views import RateDeleteViews
import debug_toolbar
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('rate/', RateListViews.as_view(), name="rate-list"),
    path('rate2/', Rate2ListViews.as_view(), name="rate-list2"),
    path('kurs/', KursListViews.as_view(), name="kurs-list"),
    path('rate/create/', RateCreateViews.as_view(), name="rate-create"),
    path('rate/create2/', Rate2CreateViews.as_view(), name="rate-create2"),
    path('rate/details/<int:pk>', RateDetailViews.as_view(), name="rate-details"),
    path('rate/details2/<int:pk>', Rate2DetailViews.as_view(), name="rate-details2"),
    path('rate/update/<int:pk>', RateUpdateViews.as_view(), name="rate-update"),
    path('rate/update2/<int:pk>', Rate2UpdateViews.as_view(), name="rate-update2"),
    path('rate/delete/<int:pk>', RateDeleteViews.as_view(), name="rate-delete"),

]
