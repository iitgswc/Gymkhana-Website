from django.contrib import admin

# Register your models here.
from .models import Clubs,Boards,Achivements,Announcements
from django_summernote.admin import SummernoteModelAdmin

class SomeModelAdmin(SummernoteModelAdmin):
    pass
class SomeModelAdmin2(SummernoteModelAdmin):
    pass

admin.site.register(Clubs,SomeModelAdmin)
admin.site.register(Boards,SomeModelAdmin2)
admin.site.register(Achivements)
admin.site.register(Announcements)