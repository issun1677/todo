from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
	user = models.ForeignKey(User, 
		on_delete=models.CASCADE, 
		null=True, 
		blank=False)
	title = models.CharField(max_length=100, blank=False)
	desc = models.TextField(max_length=300, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	completed = models.BooleanField(default=False)

	class Meta:
		verbose_name = ("Task")
		verbose_name_plural = ("Tasks")

	class Meta:
		ordering = ["completed"]
    

	def __str__(self):
		return self.title


	



	 

