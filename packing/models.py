from django.db import models
from django.db.models import F, Sum
from .managers import PackingRunManager

# Create your models here.

PLANNING_STATUS = ((0, "Planning"), (1, "Current"), (2, "Complete"))
DAYS = ((1, "Saturday"), (2, "Monday"), (3, "Tuesday"), (4, "Wednesday"), (5, "Thursday"), (6, "Friday"))
TEAMS = ["Team 1", "Team 2", "Team 3", "Twilight"]
COMPLETE = (("No", "No"), ("Yes", "Yes"))


class Pack(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="Name of the packing configuration.")
    film = models.CharField(max_length=50, help_text="Film used to seal an inner pack.")
    inner = models.CharField(max_length=50, help_text="The inner packet.")
    srp = models.CharField(max_length=50, default="No SRP", help_text="Shelf Ready Pack, usually and extra 1-for-1 cover on the inner.")
    outer = models.CharField(max_length=50, help_text="The outer box or case in which inners are packed.")

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    customer = models.CharField(max_length=50)
    packaging = models.ForeignKey(Pack, on_delete=models.CASCADE, help_text="Name of the packing configuration.")
    ppt = models.FloatField(help_text="Pieces(portions) Per Tray associated with a particular product.")
    pack_sz = models.IntegerField(help_text="How many pieces fit in an inner packet.")
    ppc = models.FloatField(help_text="Pieces Per Case")


    def __str__(self):
        return self.customer + " " + self.name + " " + str(self.pack_sz) + " x " + str(self.ppc)


class Week(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="such as: October Wk2 2022, for the second week of october.")
    start_date = models.DateField(auto_now=False, auto_now_add=False, help_text="Date the plan begins, usually a Saturday.")
    status = models.IntegerField(choices=PLANNING_STATUS, help_text="Pre-production, production, post-production.")

    class Meta:
        ordering = ['-start_date']

    def get_absolute_url(self):
        return reverse('plan-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    
class Run(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="Product Name and case qty makes sense here.")
    case_qty = models.IntegerField(help_text="The number of cases that need to be packed to meet orders.")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PackingRun(models.Model):
    name = models.ForeignKey(Run, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    day = models.IntegerField(choices=DAYS)
    time = models.IntegerField(help_text="Estimated time in minutes to complete the packing-run.")
    complete = models.CharField(max_length=50, choices=COMPLETE)

    objects = PackingRunManager()


    class Meta:
        ordering = ['day']

    def __str__(self):
        return self.week.name + " " + self.name.name