
# Create your tests here.
from django.test import TestCase
from .models import Profile 
from .models import City 
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class ProfileModelTests(TestCase):

    def test_were_cities_added(self):
        """
        were the the cities added 
        """
        user=User.objects.create_user('foo', password='bar')
        cities_in_fav = Profile.objects.create(user=user, favs=['chicago', 'denver', 'boston'])
        self.assertEqual(user.profile.favs, ['chicago', 'denver', 'boston'])

    def test_blank_fav_list(self):
        """
        testing when a user does not have a favorite list
        """
        user=User.objects.create_user('foo', password='bar')
        cities_in_fav = Profile.objects.create(user=user, favs=[])
        self.assertEqual(user.profile.favs, [])

