from django.db import models

class contact(models.Model):
    id = models.AutoField(primary_key=True) 
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=60, unique=False)
    Subject = models.CharField(max_length=50)
    Message = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"
        
    def __str__(self):
        return self.Name + "-" + self.Email