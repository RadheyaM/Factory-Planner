from django.db import models


class PackingRunQuerySet(models.QuerySet):
    def get_week(self, week_name):
        return self.filter(week__name=week_name)
    
    def get_day(self, day_name):
        return self.filter(day=day_name)


class PackingRunManager(models.Manager):
    def get_queryset(self):
        return PackingRunQuerySet(self.model, using=self._db)

    def get_week(self, week_name):
        return self.get_queryset().get_week(week_name)

    def get_day(self, day_name):
        return self.get_queryset().get_day(day_name)
