from rest_framework import serializers
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()


    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name