from django.contrib import admin
from .models import Article
# Register your models here.
# 모델에 대한 정의 
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','content','created_at','updated_at')
admin.site.register(Article,ArticleAdmin)