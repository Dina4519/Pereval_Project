from django.contrib import admin
from .models import *

class PerevalAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'add_time', 'level')

    list_filter = ('user__username', 'add_time', 'level')


admin.site.register(Coords)
admin.site.register(Level)
admin.site.register(PassUser)
admin.site.register(Pereval)
admin.site.register(Images)