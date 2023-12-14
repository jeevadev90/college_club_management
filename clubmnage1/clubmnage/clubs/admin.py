from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
class ClubAdmin(admin.ModelAdmin):
    list_display=('club_name','logo')

class DepartmentAdmin(admin.ModelAdmin):
    list_display=('name')

class MembersAdmin(admin.ModelAdmin):
    list_display=('student_name','phone_number')


admin.site.register(Club)
admin.site.register(Department)
admin.site.register(Club_members)
admin.site.register(Events)
admin.site.register(Index_content)
admin.site.register(Gallery)