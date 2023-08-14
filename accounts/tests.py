
# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from weather.models import Profile

class user_login_test(TestCase):

    def test_user_added(self):
        """
        the user added
        """
        UserModel = get_user_model()
        user = User.objects.create_user('foo', password='bar')
        
        self.assertEqual(UserModel.objects.filter(username='foo').exists(), True)

    def test_user_added_NOT_in_DB(self):
        """
         check for false entry
        """
        UserModel = get_user_model()
        self.assertEqual(UserModel.objects.filter(username='Rohan').exists(), False)

    def test_username_access(self):
        """
        access entry
        """
        user=User.objects.create_user('foo', password='bar')
        self.assertEqual(user.username, 'foo')



