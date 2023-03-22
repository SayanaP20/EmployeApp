from django.contrib import admin


# Register your models here.
from .models import *


admin.site.register(Employee)
admin.site.register( Qualification)
admin.site.register(ExperienceCertificate)
admin.site.register(DailyUpdate)