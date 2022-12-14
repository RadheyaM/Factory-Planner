from django.db import models, transaction
from django.contrib.auth.models import User
from django.db.models import F, Sum, Q
from .managers import PackingRunManager


PLANNING_STATUS = (
    (0, "Planning"),
    (1, "Current"),
    (2, "Complete"),
    (3, "Delete")
)
DAYS = (
    (1, "Saturday"),
    (2, "Monday"),
    (3, "Tuesday"),
    (4, "Wednesday"),
    (5, "Thursday"),
    (6, "Friday"),
)
COMPLETE = (("No", "NO"), ("Yes", "YES"))


class Pack(models.Model):
    """
    Model representing a particular combination of packaging
    that can be assigned to a product.
    """

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Name of the packing configuration."
    )
    film = models.CharField(
        max_length=50,
        help_text="Film used to seal an inner pack.")
    inner = models.CharField(max_length=50, help_text="The inner packet.")
    srp = models.CharField(
        max_length=50, default="No SRP", help_text="Shelf Ready Pack."
    )
    outer = models.CharField(
        max_length=50,
        help_text="The outer box or case in which inners are packed."
    )

    def __str__(self):
        return self.name


class Team(models.Model):
    """
    Model representing a packing team.
    """

    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model representing a finished product
    which can be assigned to a run.
    """

    name = models.CharField(max_length=50)
    customer = models.CharField(max_length=50)
    packaging = models.ForeignKey(
        Pack,
        on_delete=models.CASCADE,
        help_text="Name of the packing configuration."
    )
    ppt = models.FloatField(help_text="Portions Per Tray.")
    pack_sz = models.IntegerField(help_text="Portions Per Pack.")
    ppc = models.FloatField(help_text="Portions Per Case")

    def __str__(self):
        return self.customer + " " + self.name


class Week(models.Model):
    """
    Model representing a week plan.
    """

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="such as: October 2022 Wk2, for the second week of october.",
    )
    start_date = models.DateField(
        auto_now=False,
        auto_now_add=False,
        help_text="Date the plan begins,Enter as YYYY-MM-DD.",
    )
    status = models.IntegerField(
        choices=PLANNING_STATUS,
        help_text="Set Status. Select 'Delete' for Admin to action.",
    )

    class Meta:
        ordering = ["-start_date"]

    def get_absolute_url(self):
        return reverse("plan-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Run(models.Model):
    """
    Model representing a run of a particular product
    which can be assigned to a week plan.
    """

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Customer, Name & cases e.g. 'Charducks Trillionaire 230'",
    )
    case_qty = models.IntegerField(
        help_text="The number of cases that need to be packed to meet orders."
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        help_text="Select a Product to add to this Run.",
    )

    def __str__(self):
        return self.name


class PackingRun(models.Model):
    """
    Model representing Runs that have been assigned to a
    particular week plan.
    """

    name = models.ForeignKey(
        Run, on_delete=models.CASCADE, help_text="Click Field To See Choices"
    )
    week = models.ForeignKey(
        Week,
        on_delete=models.CASCADE,
        help_text="Automatically Chooses Correct Plan Week",
    )
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, help_text="Click Field To See Choices"
    )
    day = models.IntegerField(
        choices=DAYS,
        help_text="Click Field To See Choices"
    )
    time = models.IntegerField(
        help_text="Estimated time in minutes to complete the packing-run."
    )
    notes = models.TextField(blank=True, null=True, help_text="Optional")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_when = models.DateTimeField(auto_now=True)
    complete = models.CharField(max_length=50, choices=COMPLETE, default="No")

    # Custom model manager
    objects = PackingRunManager()

    class Meta:
        ordering = ["day"]

    def __str__(self):
        return self.week.name + " " + self.name.name
