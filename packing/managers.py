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
    def get_team_times(self, week_id):
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

    def get_calc_trays(self):
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
        )


class PackingRunManager(models.Manager):
    def get_queryset(self):
        return PackingRunQuerySet(self.model, using=self._db)

    def get_team_times(self, week_id):
        return self.get_queryset().get_team_times(week_id)

    def get_team_day_times(self, week_id):
        return self.get_queryset().get_team_day_times(week_id)

    def get_calc_trays(self):
        return self.get_queryset().get_calc_trays()
