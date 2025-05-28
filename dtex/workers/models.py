
from django.db import models

class Worker(models.Model):
    EMPLOYEE_TYPE_CHOICES = [
        ('Employee', 'Employee'),
        ('Contractor', 'Contractor'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=EMPLOYEE_TYPE_CHOICES)

    def __str__(self):
        return self.name


class WorkerActivity(models.Model):
    ACTIVITY_TYPE_CHOICES = [
        ('File access', 'File access'),
        ('Network connection', 'Network connection'),
        ('Application launch', 'Application launch'),
    ]

    RISK_LEVEL_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='activities')
    datetime = models.DateTimeField()
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPE_CHOICES)
    risk_level = models.CharField(max_length=10, choices=RISK_LEVEL_CHOICES)

    def __str__(self):
        return f"{self.worker.name} - {self.activity_type} ({self.risk_level})"
