from django.db import models



# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null="true")
    email = models.EmailField(max_length=100, null="true")
    password = models.CharField(max_length=128, null="true")
    contact_number = models.CharField(max_length=15, null="true")
    date_of_birth = models.DateField(null="true")
    # salary = models.DecimalField(max_digits=10, decimal_places=2, null="true")
    salary = models.IntegerField(null="true")
    designation = models.CharField(max_length=100, null="true")
    department = models.CharField(max_length=100, null="true")
    
    def __str__(self):
        return self.name
 
class Qualification(models.Model):
    employee= models.ForeignKey(Employee, on_delete=models.CASCADE, null="true")
    degree_name = models.CharField(max_length=100, null="true")
    institute_name = models.CharField(max_length=100, null="true")
    passing_year = models.IntegerField(null="true")
    percentage = models.FloatField(null="true")
    
    def __str__(self):
        return self.degree_name

class ExperienceCertificate(models.Model):
    employee= models.ForeignKey(Employee, on_delete=models.CASCADE,null="true")
    certificate = models.FileField(upload_to='certificates/', null="true")
    

# add daily_updates
class DailyUpdate(models.Model):
    employee= models.ForeignKey(Employee, on_delete=models.CASCADE,null="true")
    date = models.DateField(null="true")
    task = models.CharField(max_length=255, null="true")