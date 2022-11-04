from django.db import models

# Create your models here.

PLANNING_STATUS = ((0, "Planning"), (1, "Current"), (2, "Complete"))
DAYS = (("Saturday", "Saturday"), ("Monday", "Monday"), ("Tuesday", "Tuesday"), ("Wednesday", "Wednesday"), ("Thursday", "Thursday"), ("Friday", "Friday"))
TEAMS = ((1, "Team 1"), (2, "Team 2"), (3, "Team 3"), (4, "Team 4"))
COMPLETE = (("No", "No"), ("Yes", "Yes"))


class Packaging(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="Name of the packing configuration.")
    film = models.CharField(max_length=50, help_text="Film used to seal an inner pack.")
    inner = models.CharField(max_length=50, help_text="The inner packet.")
    srp = models.CharField(max_length=50, default="No SRP", help_text="Shelf Ready Pack, usually and extra 1-for-1 cover on the inner.")
    outer = models.CharField(max_length=50, help_text="The outer box or case in which inners are packed.")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    customer = models.CharField(max_length=50)
    packaging = models.ForeignKey(Packaging, on_delete=models.CASCADE, help_text="Name of the packing configuration.")
    ppt = models.IntegerField(help_text="Pieces(portions) Per Tray associated with a particular product.")
    pack_sz = models.IntegerField(help_text="How many pieces fit in an inner packet.")
    ppc = models.IntegerField(help_text="Pieces Per Case")

    def __str__(self):
        return self.customer + " " + self.name + " " + str(self.pack_sz) + " x " + str(self.ppc)


class Week(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="such as: October Wk2 2022, for the second week of october.")
    start_date = models.DateField(auto_now=False, auto_now_add=False, help_text="Date the plan begins, usually a Saturday.")
    status = models.IntegerField(choices=PLANNING_STATUS, help_text="Pre-production, production, post-production.")

    def __str__(self):
        return self.name


class Run(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="Product Name and case qty makes sense here.")
    case_qty = models.IntegerField(help_text="The number of cases that need to be packed to meet orders.")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Packing(models.Model):
    name = models.ForeignKey(Run, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    team = models.IntegerField(choices=TEAMS)
    day = models.CharField(max_length=50, choices=DAYS)
    time = models.IntegerField(help_text="Estimated time in minutes to complete the packing-run.")
    complete = models.CharField(max_length=50, choices=COMPLETE)

    def __str__(self):
        return self.week.name + " " + self.name.name 