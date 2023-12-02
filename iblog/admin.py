from django.contrib import admin
from .models import *


# Register your models here.

# configure of catagory means we want to show specific data at admin pannel
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('img_tag', 'title', 'desc', 'url', 'add_date', 'update_date')
    # add serch field
    search_fields = ('title', 'add_date')


# pass custome catogoryadmin clss also at time of register bcz when register occure that time it give prefrence this model Catagory is also main model
admin.site.register(Category, CatagoryAdmin)


class postAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    # filter for filter data
    list_filter = ('Category',)
    list_per_page = 5
admin.site.register(Post, postAdmin)
