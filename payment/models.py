from django.db import models
from custom_auth.models import User
from images.models import Image

# Create your models here.
class order(models.Model):
	image=models.ForeignKey(Image, on_delete=models.CASCADE)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	order_id=models.CharField(max_length=50)
	amount=models.IntegerField()
	status=models.BooleanField(default=0)
	rp_order_id=models.CharField(max_length=500, default='')
	rp_payment_id=models.CharField(max_length=500, default='')
	rp_signature=models.CharField(max_length=600, default='')