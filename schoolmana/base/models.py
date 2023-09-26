from django.db import models

# Create your models here.
class School(models.Model):
    school_id = models.IntegerField()
    school_admin = models.CharField()

class Room(models.Model):
    class_id = models.IntegerField()
    class_name = models.IntegerChoices()
    class_div = models.CharField(max_length=2)
    class_rep = models.CharField(max_length=40, null=True, blank=True)

# class Students(models.Model):
