from django.contrib import admin
# Register your models here.
from books.models import Publisher,Author,Book

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','email')
	search_fields = ('first_name','last_name')

class PublisherAdmin(admin.ModelAdmin):
	list_display = ('name','address','website')
	search_fields = ('name',)

class BookAdmin(admin.ModelAdmin):
	list_display = ('title','publisher','publication_date')
	search_fields = ('title',)
	list_filter = ('publication_date',)
	date_hierarchy = 'publication_date'
	ordering = ('-publication_date',)
	#fileds = ('title','authors','publisher',) # to others
	filter_horizontal = ('authors',)	# x-heng
	#filter_vertical = ('authors',) # y-zong 	# For ManyToMany two Frame
	raw_id_fields = ('publisher',) # For Foregin pull_down to text


admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)