from django.contrib import admin
import models

class FrontImageAdmin(admin.ModelAdmin):
    #list_display = ['title','slug','published','published_by']
    #prepopulated_fields = {"slug": ("title",)}
    pass

admin.site.register(models.FrontImage, FrontImageAdmin)
