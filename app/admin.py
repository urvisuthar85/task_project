from django.contrib import admin
from .models import User 
# Register your models here.
admin.site.register(User)
from .models import UsrRegModel
# Register your models here.
admin.site.register(UsrRegModel)