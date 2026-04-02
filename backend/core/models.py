from django.db import models

class Child(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    parent_name = models.CharField(max_length=255, blank=True, default="")
    parent_phone = models.CharField(max_length=255, blank=True, default="")
    parent_email = models.EmailField(blank=True, default="")
    group = models.CharField(max_length=50, choices=[("infant", "Infant"), ("toddler", "Toddler"), ("preschool", "Preschool"), ("after_school", "After School")], default="infant")
    allergies = models.TextField(blank=True, default="")
    status = models.CharField(max_length=50, choices=[("enrolled", "Enrolled"), ("waitlisted", "Waitlisted"), ("graduated", "Graduated")], default="enrolled")
    joined_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class DaycareParent(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    children_count = models.IntegerField(default=0)
    emergency_contact = models.CharField(max_length=255, blank=True, default="")
    address = models.TextField(blank=True, default="")
    billing_status = models.CharField(max_length=50, choices=[("current", "Current"), ("overdue", "Overdue"), ("prepaid", "Prepaid")], default="current")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class DaycareAttendance(models.Model):
    child_name = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)
    check_in = models.DateField(null=True, blank=True)
    check_out = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[("present", "Present"), ("absent", "Absent"), ("late", "Late"), ("half_day", "Half Day")], default="present")
    notes = models.TextField(blank=True, default="")
    marked_by = models.CharField(max_length=255, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.child_name
