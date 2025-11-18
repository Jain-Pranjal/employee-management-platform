from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100,unique=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    title = models.CharField(max_length=100,unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

