from django.contrib import admin

# Register your models here.
from .models import MPStrategy,MPDetails


admin.site.register(MPStrategy)
admin.site.register(MPDetails)

