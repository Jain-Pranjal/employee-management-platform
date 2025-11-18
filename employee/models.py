from django.db import models

class baseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Department(baseModel):
    name = models.CharField(max_length=100,unique=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(baseModel):
    title = models.CharField(max_length=100,unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Employee(baseModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

