from django.contrib import admin
from .models import MySkill,Service,Portfolio
from django.utils.html import format_html

class MySkillAdmin(admin.ModelAdmin):
    list_display = ('id','skill','percent')
    
admin.site.register(MySkill,MySkillAdmin)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','title','description')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="60" style="border-radius:50px;"/>'.format(object.image.url))

    thumbnail.short_description = 'Project-Image'
    list_display = ('id','title','thumbnail','description','created_date')