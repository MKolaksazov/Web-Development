from django.db import models


from django.contrib.auth.models import User

class Object(models.Model):
    name = models.CharField(max_length=100)
    ratings = models.ManyToManyField(User, through='Rating')

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rated_object = models.ForeignKey(Object, on_delete=models.CASCADE)
    value = models.SmallIntegerField(choices=[(-1, '-'), (1, '+')])

    class Meta:
        unique_together = ['user', 'rated_object']



# Create your models here.
