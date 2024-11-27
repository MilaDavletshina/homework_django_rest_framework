from django.contrib import admin

from materials.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "image")
    search_fields = ("name",)
    search_filter = ("name",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "preview", "video_link")
    search_fields = ("name",)
    search_filter = ("name",)
