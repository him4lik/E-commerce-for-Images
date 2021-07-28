from django.db import models
from custom_auth.models import User
# Create your models here

class Image(models.Model):
	file=models.ImageField(upload_to='images/')
	artist=models.ForeignKey(User, on_delete=models.CASCADE, related_name='image_to_sell')
	cart_user=models.ManyToManyField(User, blank=True)
	amount=models.IntegerField()

	def __str__(self):
		return str(self.file)


class Tag(models.Model):
	name=models.CharField(max_length=20)
	image=models.ForeignKey(Image, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
