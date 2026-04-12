from django.contrib import admin

from authors.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'gender', 'created_at', 'updated_at')
    list_filter = ('gender', 'created_at', 'updated_at')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at', 'updated_at')
