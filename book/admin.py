from django.contrib import admin
from book.models import Publisher, Author, Book

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'email']
	search_fields = ['first_name', 'last_name']

class PublisherAdmin(admin.ModelAdmin):
	list_display = ['name', 'website']

class BookAdmin(admin.ModelAdmin):
	list_display = ['name', 'publisher', 'published_date']
	list_filter = ['published_date', 'author']
	filter_horizontal = ['author']
	raw_id_fields = ['publisher']
	ordering = ['-published_date']
	date_hierarchy = 'published_date'

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)