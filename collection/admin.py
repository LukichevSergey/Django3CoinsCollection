from django.contrib import admin

from .models import *

class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class CoinAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug', 'group', 'price', 'year', 'denomination', 'diameter', 'edition', 'material', 'weight') #Поля для отображения в админке
    list_display_links = ('title',)  #Поля - ссылки
    search_fields = ('title',)  #Поля для поиска
    list_filter = ('group','year', 'material') #По каким полям фильтровать

admin.site.register(Group, GroupAdmin)
admin.site.register(Coin, CoinAdmin)

