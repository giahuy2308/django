from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Account)
admin.site.register(MainPage)
admin.site.register(Blog)
admin.site.register(Comment)