from django.contrib import admin

from materials.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "image")
    search_fields = ("name",)
    search_filter = ("name",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "preview", "video_link")
    search_fields = ("name",)
    search_filter = ("name",)