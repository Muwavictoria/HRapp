from django.contrib import admin
from . import models

# Register models.Menu your models here.
admin.site.register(models.Menu)
admin.site.register(models.Table)
# admin.site.register(models.CustomUser)
admin.site.register(models.Order)
admin.site.register(models.Dishes)
admin.site.register(models.Feedback)
admin.site.register(models.dish_feedback)