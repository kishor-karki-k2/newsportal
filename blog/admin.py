from django.contrib import admin

# Register your models here.
from.models import Category,Blog
admin.site.register([Category,Blog])