from django.db import models
from feeapp.models import Company, State, District, Qualification, Course

class Student(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
   


    YOUR_CHOICES = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    ]
    installment_type = models.CharField(max_length=200,choices=YOUR_CHOICES, default='option1')
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    

class Receipt(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.student.name