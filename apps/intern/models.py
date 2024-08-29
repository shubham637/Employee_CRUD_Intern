from django.db import models
from Employee_CRUD_Intern.custom_models import DateTimeModel



class Employee(DateTimeModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField()
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    start_date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.position}'