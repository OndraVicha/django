from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

def attachment_path(instance, filename):
    return "tank/" + str(instance.tank.id) + "/attachments/" + filename
def poster_path(instance, filename):
    return "tank/" + str(instance.id) + "/poster/" + filename
# Create your models here.
class Countrie(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Country",help_text='Enter a country from where is the tank')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Companie(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Company",help_text='Enter a company name')
    info = models.TextField(blank=True, null=True, verbose_name="Info")
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Crew(models.Model):
    name = models.CharField(max_length=50, unique=False, verbose_name="Name", help_text='Enter a crewman name')
    surname = models.CharField(max_length=50, unique=True, verbose_name="Surname", help_text='Enter a crewman surname')
    birth_date = models.DateField(blank=True, null=True,
                                  help_text="Please use the following format: <em>YYYYMM-DD</em>.",
                                  verbose_name="Date of birth")

    TANK_ROLE = (
        ('driver', 'Driver'),
        ('commander', 'Commander'),
        ('gunner', 'Gunner'),
        ('loader', 'Loader'),
    )
    tank_type = models.CharField(max_length=10, choices=TANK_ROLE, blank=True,
                                 help_text='Select crewman role', verbose_name="Tank role")

    class Meta:
        ordering = ["-birth_date", "name"]

    def __str__(self):
        return f"{self.name}, year: {str(self.birth_date.year)}"


class Machine(models.Model):
    name = models.CharField(max_length=200, verbose_name="Tank",help_text='Enter a specific tank name')
    max_speed = models.IntegerField(blank=True, null=True, help_text="Please enter an integer value (km/h)",
                                  verbose_name="Maximal speed")
    weight = models.IntegerField(blank=True, null=True, help_text="Please enter an integer value (tons)",
                                       verbose_name="Weight")
    penetration = models.IntegerField(blank=True, null=True, help_text="Please enter an integer value (millimeters)",
                                   verbose_name="Penetration")
    crew = models.ManyToManyField(Crew, help_text='Select a tankcrew for this tank')
    class Meta:
            ordering = ["name"]
    def __str__(self):
        return self.name


class Tank(models.Model):
    tank = models.CharField(max_length=200, verbose_name="Tank", help_text='Enter a tank name')
    history = models.TextField(blank=True, null=True, verbose_name="History")
    creation_date = models.DateField(blank=True, null=True,
                                     help_text="Please use the following format: <em>DD.MM.YYYY</em>.",
                                     verbose_name="First tank made")
    company_name = models.ForeignKey(Companie, on_delete=models.CASCADE)
    country = models.ForeignKey(Countrie, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine,on_delete=models.CASCADE)

    TANK_TYPE = (
        ('light tank', 'Light tank'),
        ('medium tank', 'Medium tank'),
        ('heavy tank', 'Heavy tank'),
        ('tank destroyer', 'Tank destroyer'),
        ('anti air tank', 'Anti air tank'),
    )
    tank_type = models.CharField(max_length=15, choices=TANK_TYPE, blank=True, help_text='Select tank type',
                                 verbose_name="Tank type")

    class Meta:
        ordering = ["-creation_date", "tank"]

    def __str__(self):
        return f"{self.tank}, year: {str(self.creation_date.year)}"
