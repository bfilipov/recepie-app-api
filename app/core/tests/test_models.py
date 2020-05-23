from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successgful(self):
        """Test creating a new user with an email is successful"""
        email = 'bacebogo@abv.bg'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that the email domain for a new user is normalized to case insensitive"""
        email = 'bacebogo@ABV.BG'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, 'bacebogo@abv.bg')

    def test_new_user_invalid_email(self):
        """test creating user without email raises ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='123'
            )

    def test_create_new_superuser(self):
        """test creating a new super user   """
        user = get_user_model().objects.create_superuser(
            email='adminbace@gmail.com',
            password='edno dve tri'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

