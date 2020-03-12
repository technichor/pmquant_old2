from django.contrib import admin
from .models import idea
# Register your models here.

@admin.register(idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','author','elo_score','created')
    list_filter = ('status','created','modified','release')
    search_fields = ('title', 'author', 'description')
    # raw_id_fields = ()
    # date_hiearchy = 'created'
    ordering = ('-created','title')