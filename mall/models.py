from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class Shop(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=100)
	phone = models.CharField(max_length=11)
	address = models.TextField()
	content = models.TextField()
	photo1 = models.ImageField()
	photo2 = models.ImageField(blank=True)
	photo3 = models.ImageField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class Review(models.Model):
	shop = models.ForeignKey(Shop)
	user = models.ForeignKey(User)
	content = models.TextField()
	photo = models.ImageField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.content