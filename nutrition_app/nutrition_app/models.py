from django.db import models

class Doctor(models.Model):
    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}: {self.firstName} {self.lastName}"



class Patient(models.Model):
    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.id + ": " + self.firstName + " " + self.lastName


class Measurement(models.Model):
    id = models.AutoField(primary_key=True)
    patientId = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    weight_uom = models.CharField(max_length=20)
    bmi = models.DecimalField(max_digits=4, decimal_places=1)
    fat_pct = models.DecimalField(max_digits=4, decimal_places=1)
    muscle_pct = models.DecimalField(max_digits=4, decimal_places=1)
    v_fat = models.DecimalField(max_digits=4, decimal_places=1)
    waist = models.DecimalField(max_digits=5, decimal_places=1)
    hip = models.DecimalField(max_digits=5, decimal_places=1)
    length_uom = models.CharField(max_length=20)

    def __str__(self):
        return self.id + ": " + self.bmi



class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    patientId = models.IntegerField()
    doctorId = models.IntegerField()
    date_time = models.DateTimeField()
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.id + ": " + self.date_time

class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    measurementId = models.IntegerField()
    appointmentId = models.IntegerField()
    plan_detail = models.CharField(max_length=200)

    def __str__(self):
        return self.id + ": " + self.plan_detail
