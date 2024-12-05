from rest_framework.serializers import ValidationError


def validate_video_url(value):
    if value.lower() != 'www.youtube.com' and value.lower() != 'youtube.com':
        raise ValidationError("Cсылки на сторонние образовательные платформы или личные сайты — запрещены!")
