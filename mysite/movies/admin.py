from django.contrib import admin
from .models import Title

class TitleAdmin(admin.ModelAdmin):
  search_fields = ['title__search', 'year']
  list_display = ('id', 'title', 'year')
  list_filter = [ 'title', 'year' ]

admin.site.register(Title, TitleAdmin)
