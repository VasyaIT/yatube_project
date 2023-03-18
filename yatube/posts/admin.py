from django.contrib import admin

from .models import Group, Post, Contact


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'email', 'subject', 'body', 'is_answered')
    empty_value_display = '-пусто-'


admin.site.register(Contact, ContactAdmin)
