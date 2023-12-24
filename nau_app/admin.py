from django.contrib import admin

# Register your models here.
from nau_app.models import Article


# 设置admin界面展示的样式
class ArticleAdmin(admin.ModelAdmin):
    list_display  = ("title", "data", "pub_date")

admin.site.register(Article, ArticleAdmin)