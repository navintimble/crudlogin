from django.contrib import admin

# Register your models here.
from .models import User, Employee

admin.site.register((User, Employee))
