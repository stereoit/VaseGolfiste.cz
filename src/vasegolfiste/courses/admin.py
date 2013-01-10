from django.contrib import admin
import models

class GolfCourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'location']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.GolfCourse, GolfCourseAdmin)

