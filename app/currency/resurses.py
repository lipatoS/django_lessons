from import_export import resources
from currency.models import Rate


class RateResource(resources.ModelResource):
    class Meta:
        model = Rate
        fields = (
            "id",
            "name",
            "surname",
            "salary",
            "state",
            "child",
            "date",
        )
