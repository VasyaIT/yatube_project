from django.contrib import admin
from .models import Post, Contact


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email', 'subject', 'body', 'is_answered')
    empty_value_display = '-пусто-'


admin.site.register(Contact, ContactAdmin)

