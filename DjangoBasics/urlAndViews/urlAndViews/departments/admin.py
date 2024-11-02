from django.contrib import admin

from urlAndViews.departments.models import Department


# Register your models here.
@admin.register(Department)
class Admin(admin.ModelAdmin):
    pass