from django.contrib import admin
from .models import Image, Tag

# Register your models here.
class imageadmin(admin.ModelAdmin):
	list_display = ( 'id','artist', 'amount','file')


class tagadmin(admin.ModelAdmin):
	list_display = ('name','image')



admin.site.register(Image, imageadmin)
admin.site.register(Tag, tagadmin)
