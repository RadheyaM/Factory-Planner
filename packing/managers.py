from django.db import models
from django.db.models import (
    Sum,
    F,
    Value,
    ExpressionWrapper,
    FloatField,
    DecimalField
    )


class PackingRunQuerySet(models.QuerySet):
    """
    Custom Queries related to the PackingRun Model.
    To be fed into the PackingRunManager class below.
    """

    def get_team_times(self, week_id):
        """
        Function takes in a week id number and returns
        a list of sums of the minutes per team for that week.
        """
        times = []
        for team in range(1, 5):
            filtered = self.filter(team=team, week=week_id)
            try:
                val = filtered.aggregate(Sum("time"))["time__sum"]
                if val is None:
                    time.append(0)
                else:
                    times.append(val)
            except Exception:
                times.append(0)
        return times

    def get_team_day_times(self, week_id):
        """
        Function that takes in a week id number and returns
        a list of minutes per team per day.

        """
        times = []
        for team in range(1, 5):
            for day in range(1, 7):
                filtered = self.filter(team=team, day=day, week=week_id)
                try:
                    val = filtered.aggregate(Sum("time"))["time__sum"]
                    if val is None:
                        time.append(0)
                    else:
                        times.append(val)
                except Exception:
                    times.append(0)
        return times

    def get_calcs(self):
        """
        A function to create some annotated rows with custom calculations
        relating to the PackingRun model.
        """
        return self.annotate(
            trays=ExpressionWrapper(
                (F("name__product__ppc") / F("name__product__ppt"))
                * F("name__case_qty"),
                output_field=FloatField(),
            ),
            est_packets=ExpressionWrapper(
                F("name__product__pack_sz") * F("name__case_qty"),
                output_field=FloatField(),
            ),
            film_rolls=ExpressionWrapper(
                (F("name__product__pack_sz") * F("name__case_qty")) / 1000,
                output_field=FloatField(),
            ),
        )


class PackingRunManager(models.Manager):
    """
    PackingRunManager used for custom queries sent to the
    the detail template.  Implemented to cut bloat in the
    views.py file.
    """
    def get_queryset(self):
        return PackingRunQuerySet(self.model, using=self._db)

    def get_team_times(self, week_id):
        return self.get_queryset().get_team_times(week_id)

    def get_team_day_times(self, week_id):
        return self.get_queryset().get_team_day_times(week_id)

    def get_calc_trays(self):
        return self.get_queryset().get_calc_trays()
