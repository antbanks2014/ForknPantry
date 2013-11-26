from django.db import models

# Ingredient Model
class Ingredient(models.Model):
        name = models.CharField(max_length=200)

# Category Model
class Category(models.Model):
        name = models.CharField(max_length=200)

# User Model
class User(models.Model):
	email = models.EmailField(max_length=254)
	password_hash = models.CharField(max_length=200)
	session_id = models.IntegerField()
	ingredients = models.ManyToManyField(Ingredient)

# Recipe Model
class Recipe(models.Model):
	name = models.CharField(max_length=200)
	link = models.URLField()
	photo_exists = models.BooleanField()
	category = models.ForeignKey(Category)
	ingredients = models.ManyToManyField(Ingredient)