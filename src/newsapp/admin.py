from django.contrib import admin
from .models import Category,News,Comment
from import_export import resources
from import_export.admin import ImportExportModelAdmin

admin.site.register(Category)

class AdminNews(admin.ModelAdmin):
    list_display=('title', 'category', 'add_time')

admin.site.register(News,AdminNews)

class AdminComment(admin.ModelAdmin):
    list_display=('news', 'email', 'comment','status')

admin.site.register(Comment,AdminComment)

# class showAIres(resources.ModelResource):
#     class Meta:
#         model = showAI
# class showAIAdmin(ImportExportModelAdmin):
#     resource_class = showAIres
#     list_display = ['state_no', 'crop_name' ,'yieldd']
# admin.site.register(showAI,showAIAdmin)











