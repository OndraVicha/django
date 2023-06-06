from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Countrie)

admin.site.register(Companie)

admin.site.register(Crew)

admin.site.register(Machine)

admin.site.register(Tank)

admin.site.register(Attachment)
