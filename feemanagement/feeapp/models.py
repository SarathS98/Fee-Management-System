from django.db import models



class State(models.Model):
    state = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.state
    

class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district_name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.district_name

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    address3 = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    logo = models.ImageField(upload_to='company_logos', blank=True, null=True)
    website = models.URLField()
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.company_name

class Qualification(models.Model):
    qualification = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.qualification

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name


class Master_data(models.Model):
    name = models.CharField(max_length=20)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    type = models.CharField(max_length=100, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


