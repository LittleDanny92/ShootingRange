from django.contrib import admin
from reservation_form.models import BookedDate

class BookedDateAdmin(admin.ModelAdmin):
    pass

admin.site.register(BookedDate, BookedDateAdmin)