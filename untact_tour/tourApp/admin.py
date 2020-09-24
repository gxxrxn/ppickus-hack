from django.contrib import admin
from .models import Users, Videos, Categories

# Register your models here.
admin.site.register(Users)
admin.site.register(Videos)
admin.site.register(Categories)