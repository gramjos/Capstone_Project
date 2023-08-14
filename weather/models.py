from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class City(models.Model):
    name = models.CharField(max_length=25)
    # specify blank=True to indicate that this field is optional
    #user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True,default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'

# Django provides a built in user model that we already using. This model is associated with that one
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE )
        # blank=True         b/c not all users will have a fav list
        # null=True          when blank we expect null
        # on_delete=models.CASCADE      when a user get deletes all of the Prolfile model data will be deleted as well

    favs = ArrayField(
            models.CharField(max_length=30, blank=True),    # Each city can be up to 30 characters. This can be blank for user that do not have any fav items
            size=512            # a user can have up to 512 fav items 
            )

    # alter the string repersentation when the object is called
    def __str__(self):
        return str(self.user) 

class CityList(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

