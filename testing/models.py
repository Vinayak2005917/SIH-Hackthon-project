from django.db import models

class Data(models.Model):
    Name = models.CharField(max_length=25)
    Number = models.CharField(max_length=25)
    Email = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Name}, {self.Number}, {self.Email}" 
    
    def __str__(self):
        return self.Name