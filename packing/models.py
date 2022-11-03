from django.db import models

# Create your models here.

PLANNING_STATUS = ((0, "Planning"), (1, "Current"), (2, "Complete"))
DAYS = ((1, "Saturday"), (2, "Monday"), (3, "Tuesday"), (4, "Wednesday"), (5, "Thursday"), (6, "Friday"))
TEAMS = ((1, "Team 1"), (2, "Team 2"), (3, "Team 3"), (4, "Team 4"))
COMPLETE = ((1, "No"), (2, "Yes"))


class Packaging(models.Model):
    name = models.CharField(("Packing Configuration"), max_length=50, unique=True)
    film = models.CharField(("Film"), max_length=50)
    inner = models.CharField(("Inner Packaging"), max_length=50)
    srp = models.CharField(("Shelf Ready Pack"), max_length=50, default="No SRP")
    outer = models.CharField(("Outer Case"), max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(("Product Name"), max_length=50)
    customer = models.CharField(("Customer"), max_length=50)
    packaging = models.ForeignKey(Packaging, on_delete=models.CASCADE)
    ppt = models.IntegerField(("Pieces Per Tray"))
    pack_sz = models.IntegerField(("Pack Size"))
    ppc = models.IntegerField(("Packs Per Case"))

    def __str__(self):
        return self.customer + " " + self.name + " " + self.pack_sz + " x " + self.ppc


class Week(models.Model):
    name = models.CharField(("Week Code"), max_length=50, unique=True)
    start_date = models.DateField(("Start Date"), auto_now=False, auto_now_add=False)
    status = models.IntegerField(choices=PLANNING_STATUS)

    def __str__(self):
        return self.name


class Run(models.Model):
    name = models.CharField(("Run Name"), max_length=50, unique=True)
    case_qty = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    trays = models.IntegerField()
    time = models.IntegerField()
    complete = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Packing(models.Model):
    name = models.ForeignKey(Run, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    team = models.IntegerField(choices=TEAMS)
    day = models.IntegerField(choices=DAYS)

    def __str__(self):
        return self.week + " " + self.name