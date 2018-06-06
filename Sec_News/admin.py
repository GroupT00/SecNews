from django.contrib import admin
from Sec_News.models import NewsSql
class SecNewsAdmin(admin.ModelAdmin):
	list_display = ('Art_time','Art_title','Art_type','Art_exa')
admin.site.register(NewsSql,SecNewsAdmin)