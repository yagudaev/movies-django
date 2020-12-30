from django.contrib import admin
from .models import Title

class TitleAdmin(admin.ModelAdmin):
  list_display = ('id', 'title')
  list_filter = [ 'title', 'year' ]

admin.site.register(Title, TitleAdmin)
