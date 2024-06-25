from django.contrib import admin
from phones.models import Phone


@admin.register(Phone)
class AdminPhone(admin.ModelAdmin):
    pass
