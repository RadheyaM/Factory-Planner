from django.db import models

# Create your models here.

PLANNING_STATUS = ((0, "Planning"), (1, "Current"), (2, "Complete"))
DAYS = (("Saturday", "Saturday"), ("Monday", "Monday"), ("Tuesday", "Tuesday"), ("Wednesday", "Wednesday"), ("Thursday", "Thursday"), ("Friday", "Friday"))
TEAMS = ((1, "Team 1"), (2, "Team 2"), (3, "Team 3"), (4, "Team 4"))
COMPLETE = (("No", "No"), ("Yes", "Yes"))


class Packaging(models.Model):
    name = models.CharField(max_length=50, unique=True)
    film = models.CharField(max_length=50)
    inner = models.CharField(max_length=50)
    srp = models.CharField(max_length=50, default="No SRP")
    outer = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    customer = models.CharField(max_length=50)
    packaging = models.ForeignKey(Packaging, on_delete=models.CASCADE)
    ppt = models.IntegerField()
    pack_sz = models.IntegerField()
    ppc = models.IntegerField()

    def __str__(self):
        return self.customer + " " + self.name + " " + str(self.pack_sz) + " x " + str(self.ppc)


class Week(models.Model):
    name = models.CharField(max_length=50, unique=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    status = models.IntegerField(choices=PLANNING_STATUS)

    def __str__(self):
        return self.name


class Run(models.Model):
    name = models.CharField(max_length=50, unique=True)
    case_qty = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Packing(models.Model):
    name = models.ForeignKey(Run, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    team = models.IntegerField(choices=TEAMS)
    day = models.CharField(max_length=15, choices=DAYS)
    time = models.IntegerField()
    complete = models.CharField(max_length=5, choices=COMPLETE)

    def __str__(self):
        return self.week.name + " " + self.name.name 