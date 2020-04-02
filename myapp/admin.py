from django.contrib import admin

# Register your models here.

from myapp.models import MyModel,Remedy

admin.site.register(MyModel)
admin.site.register(Remedy)

