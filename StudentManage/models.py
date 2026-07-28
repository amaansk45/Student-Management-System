from django.db import models

class Student(models.Model):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    course = models.CharField(max_length=20)
    age = models.IntegerField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="active"
    )
