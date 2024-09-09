from django.contrib import admin

from . import models

admin.site.register(models.Patient)
admin.site.register(models.Doctor)
admin.site.register(models.Measurement)
admin.site.register(models.Appointment)
admin.site.register(models.Plan)