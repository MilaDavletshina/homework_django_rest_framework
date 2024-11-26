from rest_framework import serializers

from materials.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        """Получает объект курса obj и возвращает количество связанных уроков"""
        return obj.lessons.count()  # Используем related_name 'lessons'

    class Meta:
        model = Course
        fields = ['name', 'lesson_count']  # указанные здесь поля будут возвращаться в postman


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"