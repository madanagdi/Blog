from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'friend', 'subject', 'publish', 'pic')
    search_fields = ('title', 'friend')
    # Register your models here.
