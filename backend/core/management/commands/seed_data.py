from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Child, DaycareParent, DaycareAttendance
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusDaycare with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusdaycare.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Child.objects.count() == 0:
            for i in range(10):
                Child.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    age=random.randint(1, 100),
                    parent_name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    parent_phone=f"+91-98765{43210+i}",
                    parent_email=f"demo{i+1}@example.com",
                    group=random.choice(["infant", "toddler", "preschool", "after_school"]),
                    allergies=f"Sample allergies for record {i+1}",
                    status=random.choice(["enrolled", "waitlisted", "graduated"]),
                    joined_date=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 Child records created'))

        if DaycareParent.objects.count() == 0:
            for i in range(10):
                DaycareParent.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    email=f"demo{i+1}@example.com",
                    phone=f"+91-98765{43210+i}",
                    children_count=random.randint(1, 100),
                    emergency_contact=f"Sample {i+1}",
                    address=f"Sample address for record {i+1}",
                    billing_status=random.choice(["current", "overdue", "prepaid"]),
                )
            self.stdout.write(self.style.SUCCESS('10 DaycareParent records created'))

        if DaycareAttendance.objects.count() == 0:
            for i in range(10):
                DaycareAttendance.objects.create(
                    child_name=f"Sample DaycareAttendance {i+1}",
                    date=date.today() - timedelta(days=random.randint(0, 90)),
                    check_in=date.today() - timedelta(days=random.randint(0, 90)),
                    check_out=date.today() - timedelta(days=random.randint(0, 90)),
                    status=random.choice(["present", "absent", "late", "half_day"]),
                    notes=f"Sample notes for record {i+1}",
                    marked_by=f"Sample {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 DaycareAttendance records created'))
