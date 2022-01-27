from asyncore import poll
from django.contrib import admin
from pollApp import models
# Register your models here.
admin.site.register(models.Poll)