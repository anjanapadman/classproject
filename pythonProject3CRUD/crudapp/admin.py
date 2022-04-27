from django.contrib import admin

# Register your models here.
from crudapp import models

admin.site.register(models.Login)
admin.site.register(models.Student)
admin.site.register(models.Book)