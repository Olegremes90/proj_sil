from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Technica(models.Model):
    title = models.CharField(max_length=150)
    descrip = models.TextField(max_length=2500)

    def __str__(self):
        return self.title
class Engine(models.Model):
    title = models.CharField(max_length=150)
    descrip = models.TextField(max_length=2500)

    def __str__(self):
        return self.title

class Transmisia(models.Model):
    title = models.CharField(max_length=150)
    descrip = models.TextField(max_length=2500)

    def __str__(self):
        return self.title
class Lead(models.Model):
    title = models.CharField(max_length=150)
    descrip = models.TextField(max_length=2500)

    def __str__(self):
        return self.title

class Steerable_Bridge(models.Model):
    title = models.CharField(max_length=150)
    descrip = models.TextField(max_length=2500)

    def __str__(self):
        return self.title

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    descrip = models.TextField(max_length=2500)

    def __str__(self):
        return self.title
class Service(models.Model):
    title = models.CharField(max_length=150)
    descrip = models.TextField(max_length=2500)

    def __str__(self):
        return self.title
class Vidi_TO(models.Model):
    title = models.CharField(max_length=150)
    descrip = models.TextField(max_length=2500)

    def __str__(self):
        return self.title



class Usel_Refusal(models.Model):
    title = models.CharField(max_length=150)
    descrip = models.TextField(max_length=2500)

    def __str__(self):
        return self.title

class Recovery(models.Model):
    title = models.CharField(max_length=150)
    descrip = models.TextField(max_length=2500)

class Machine(models.Model):
    number_machine = models.CharField(max_length=100)
    model_technic = models.ForeignKey(Technica, on_delete=models.CASCADE)
    model_engine = models.ForeignKey(Engine, on_delete= models.CASCADE)
    number_engine = models.CharField(max_length=100)
    model_transmisia = models.ForeignKey(Transmisia, on_delete=models.CASCADE)
    number_transmisia = models.CharField(max_length=100)
    lead_model = models.ForeignKey(Lead, on_delete=models.CASCADE)
    number_lead = models.CharField(max_length=100)
    model_steerable_bridge = models.ForeignKey(Steerable_Bridge, on_delete=models.CASCADE)
    number_steerable_bridge = models.CharField(max_length=100)
    contract_postavka = models.TextField(max_length=250)
    date_otgruzka = models.DateField(auto_now_add=True)
    consignee = models.TextField(max_length=250)
    adress = models.CharField(max_length=200)
    complectation = models.TextField (max_length=1000)
    client_model = models.ForeignKey(Client, on_delete=models.CASCADE)
    service_model = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.number_machine

class TO(models.Model):
    car = models.ForeignKey(Machine, on_delete=models.CASCADE)
    vid_to = models.ForeignKey(Vidi_TO, on_delete=models.CASCADE)
    data_to = models.DateField()
    narabotka = models.IntegerField()
    number_zakaza = models.CharField(max_length=100)
    data_zakaza = models.DateField(auto_now_add=True)
    service_company = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.car)

class Complaint(models.Model):
    date_refusal = models.DateField()
    working_off = models.IntegerField()
    usel = models.ForeignKey(Usel_Refusal, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    recovery = models.ForeignKey(Recovery,on_delete=models.CASCADE)
    spare_parts = models.TextField(max_length=1000)
    date_recovery = models.DateField()
    @property
    def downtime(self):
        return self.date_recovery - self.date_refusal
    car_complaint = models.ForeignKey(Machine, on_delete=models.CASCADE)
    service_org = models.ForeignKey(Service, on_delete=models.CASCADE)
