from django.contrib import admin

# Register your models here.
from .models import User,history
admin.site.register(history)



admin.site.register(User)