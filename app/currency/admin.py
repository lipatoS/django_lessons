from django.contrib import admin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from currency.models import Rate

from currency.resurses import RateResource


class RateAdmin(ImportExportModelAdmin):
    resource_class = RateResource
    list_display = (
        "id",
        "name",
        "surname",
        "salary",
        "state",
        "child",
        "date",

    )
    list_filter = (
        "name",
        "salary",
        ("date", DateRangeFilter)
    )
    search_fields = (
        "name",
        "surname",
        "state",
    )
    readonly_fields = (
        "name",
        "surname",
    )

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Rate, RateAdmin)
