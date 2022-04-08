from django.contrib import admin
from .models import Post, Category, Tag


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}




# Register your models here.
admin.site.register(Post)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)