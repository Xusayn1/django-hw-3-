from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Employee(BaseModel):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    info = models.TextField()

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        
            