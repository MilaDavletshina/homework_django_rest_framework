from django.contrib import admin

from users.models import User, Payments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "first_name", "last_name", "phone", "city", "avatar")


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ("user", "payment_date", "paid_course", "paid_lesson", "payment_amount", "payment_method")
    search_fields = ("user",)
    search_filter = ("payment_date","paid_course", "paid_lesson",)