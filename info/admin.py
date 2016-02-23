from django.contrib import admin

from models import Gig, Bio, Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'url', 'active')

admin.site.register(Gig)
admin.site.register(Bio)
admin.site.register(Video,VideoAdmin)

