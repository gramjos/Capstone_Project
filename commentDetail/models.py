from django.db import models
from django.contrib.auth.models import User
from weather.views import City, CityList
# Create your models here.

class Review(models.Model):

    text = models.CharField(max_length=100)

    date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User,on_delete=models.CASCADE)


    watchAgain = models.BooleanField()

    def __str__(self):

        return self.text


class Comment(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=180, blank=True)

    def __str__(self):
        return '%s - %s - %s' % (self.city.name, self.user.username, self.content)