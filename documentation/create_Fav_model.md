## This guide gives examples on how to search and manipulate model data 

Given Model:
```python
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    favs = ArrayField(
            models.CharField(max_length=512, blank=True),
            size=80,
        )
    def __str__(self):
        return str(self.user )
```

Lets play with this model in the django shell. 
```shell
$ python manage.py shell
```
```python
>>> from weather.models import Profile
>>> Profile.objects.all()
<QuerySet [<Profile: Graham>]>

# Create a user in shell
>>> from django.contrib.auth.models import User
>>> user=User.objects.create_user('foo', password='bar')
>>> user.save()
>>> Profile.objects.create(user=user, favs=['chicago', 'denver', 'boston'])
<Profile: foo>

# is user already in database ?
>>> from django.contrib.auth import get_user_model
>>> UserModel = get_user_model()
>>> UserModel.objects.filter(username='foo').exists()
True

# getting a user from the User model
>>> get_user_model().objects.get(username='Graham')
<User: Graham>

>>> au = get_user_model().objects.get(username='admin')
<User: admin>

# queries
>>> Profile.objects.filter(favs__contains=['boston'])
<QuerySet [<Profile: foo>]>
>>> Profile.objects.filter(favs__contains=['New York'])
<QuerySet [<Profile: Graham>]>

# given a user instance already exists 'au' create a Profile entry with it
>>> Profile.objects.create(user=au, favs=['chicago', 'Park City','Dallas', 'denver', 'boston'])
<Profile: admin>

# which users have "chciago" as a fav
>>> Profile.objects.filter(favs__overlap=["chicago"])
<QuerySet [<Profile: foo>, <Profile: admin>]>

# # list all model fields 
>>> [f.name for f in Profile._meta.get_fields()]
['id', 'user', 'favs']

# get fav list for a user
>>> au.profile.favs
['chicago', 'Park City', 'Dallas', 'denver', 'boston']
# ***NOTICE that the model has a capital P and when referenced it uses lowercase

# overwriting array list
>>> au.profile.favs
['chicago', 'Park City', 'Dallas', 'denver', 'boston']
>>> au.profile.favs = ['chicago', 'Park City', 'Dallas']
>>> au.profile.favs
['chicago', 'Park City', 'Dallas']
