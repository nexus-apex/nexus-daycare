from django.contrib import admin
from .models import Child, DaycareParent, DaycareAttendance

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "parent_name", "parent_phone", "parent_email", "created_at"]
    list_filter = ["group", "status"]
    search_fields = ["name", "parent_name", "parent_phone"]

@admin.register(DaycareParent)
class DaycareParentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "children_count", "emergency_contact", "created_at"]
    list_filter = ["billing_status"]
    search_fields = ["name", "email", "phone"]

@admin.register(DaycareAttendance)
class DaycareAttendanceAdmin(admin.ModelAdmin):
    list_display = ["child_name", "date", "check_in", "check_out", "status", "created_at"]
    list_filter = ["status"]
    search_fields = ["child_name", "marked_by"]
