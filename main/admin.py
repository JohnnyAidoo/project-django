from django.contrib import admin
from .models import Posts

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    admin.site.register(Posts)