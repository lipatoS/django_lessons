from django.contrib import admin
from django.urls import path
from currency.views import hello_world
from currency.views import gen_pass
from currency.views import raid_list
from currency.views import response_codes
from currency.views import index
from currency.views import r_create
from currency.views import r_details
from currency.views import r_update
from currency.views import r_delete

import debug_toolbar
from django.conf import settings
from django.urls import include, path


urlpatterns = [
    path('',index),
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('gen/', gen_pass),
    path('rate/', raid_list),
    path('response/', response_codes),
    path('rate/create/', r_create),
    path('rate/details/<int:rate_id>', r_details),
    path('rate/update/<int:rate_id>', r_update),
    path('rate/delete/<int:rate_id>', r_delete),


]
