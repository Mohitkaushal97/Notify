from django.db import models

# Create your models here.
class local(models.Model):
	user_id=models.CharField(max_length=8,null=False)
	lat=models.CharField(max_length=8,null=False)
	long=models.CharField(max_length=8,null=False)
	title=models.CharField(max_length=100,default='')
	body=models.CharField(max_length=100,null=False)
	device_token=models.CharField(max_length=8,null=False)



	def __str__(self):
		return u"%s %s %s %s %s %s" % (self.user_id,self.lat,self.long,self.title,self.body,self.device_token)
