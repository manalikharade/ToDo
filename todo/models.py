from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
	user = models.CharField(max_length=200)
	pwd = models.CharField(max_length=10)

	def __str__(self):
		return self.user

class ToDo(models.Model): #Table name, has to wrap models.Model to get the functionality of Django.
    user=models.ForeignKey('User',on_delete=models.CASCADE,)
    name = models.CharField(max_length=100) 
    duedate = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
 
    def __str__(self): 
        return self.name
    class Meta:
        ordering = ["-duedate"]
