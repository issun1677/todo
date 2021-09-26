from django.db import models
from django.utils import timezone

# Create your models here.
class Todotext(models.Model):
	text = models.TextField(max_length=150, blank=False)
	created = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d"))
	

	class Meta:
		ordering = ["-created"]


	class Meta:
		verbose_name= "Todotext"
		verbose_name_plural= "Todotexts"

	
	def __str__(self):
		return self.text


