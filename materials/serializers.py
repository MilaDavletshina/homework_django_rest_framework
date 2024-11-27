from rest_framework import serializers

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lesson_count(self, obj):
        """Получает объект курса obj и возвращает количество связанных уроков"""
        return obj.lessons.count()  # Используем related_name 'lessons'

    def lessons(self, obj):
        """Выдавет и количество уроков курса и информацию по всем урокам курса одновременно"""
        return obj.lesson()

    class Meta:
        model = Course
        fields = [
            "name",
            "lesson_count",
            "lessons",
        ]  # указанные здесь поля будут возвращаться в postman
