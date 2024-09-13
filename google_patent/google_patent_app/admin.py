from django.contrib import admin
from .models import GooglePatentData, NumericalStatistics, CategoricalFrequencyCount

admin.site.register(GooglePatentData)
admin.site.register(NumericalStatistics)
admin.site.register(CategoricalFrequencyCount)
# Register your models here.
