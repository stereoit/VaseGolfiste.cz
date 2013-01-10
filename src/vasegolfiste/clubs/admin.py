from django.contrib import admin
import models

class GolfClubAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.GolfClub, GolfClubAdmin)

