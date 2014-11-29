from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyUser(models.Model):
	permission = models.IntegerField()
	nickname = models.CharField(max_length=64)
	user_type = models.CharField(max_length=128)
	headimg = models.ImageField(upload_to='./image/')

	user = models.OneToOneField(User)

	class Meta:
		ording = ('nickname',)
	
	def __unicode__(self):
		return self.nickname

class Letter(models.Model):
	title = models.CharField(max_length = 64)
	context = models.TextField()
	time = models.DateTimeField(auto_now=True)
	flag = models.BooleanField(default=False)

	user_from = models.ForeignKey(MyUser)
	user_to = models.ForeignKey(MyUser)

	def __unicode__(self):
		return self.title

class ProductModel(models.Model):
	name = models.CharField(max_length=64)
	date = models.DateTimeField(auto_now=True)
	price = models.FloatField()
	pic_3D = models.URLField()
	published = models.BooleanField(default=False)

	author = models.ForeignKey(MyUser)
	favour = models.ManyToManyField(MyUser)

	def __unicode__(self):
		return self.name

class Comment(models.Model):
	context = models.TextField()
	date = models.DateTimeField(auto_now=True)
	starts = models.IntegerField()

	author = models.ForeignKey(MyUser)
	produce = models.ForeignKey(ProductModel)

	def __unicode__(self):
		return self.context

class Pic(models.Model):
	descript = models.TextField()
	img = models.ImageField()

	produce = models.ForeignKey(ProductModel)

	def __unicode__(self):
		return self.descript

class Show(models.Model):
	title = models.CharField(max_length=64)
	descript = models.TextField()
	number = models.IntegerField()
	link = models.URLField()

	picture = models.ForeignKey(Pic)

	def __unicode__(self):
		return self.descript