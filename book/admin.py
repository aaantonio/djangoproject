from django.contrib import admin
from book.models import Publisher, Author, Book

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'email']
	search_fields = ['first_name', 'last_name']

class PublisherAdmin(admin.ModelAdmin):
	list_display = ['name', 'website']

class BookAdmin(admin.ModelAdmin):
	pass

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)