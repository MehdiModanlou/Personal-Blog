from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.forms import CustomUserCreationForm


class CustomUserCreationFormTests(TestCase):
    def test_custom_user_creation_form_valid(self):
        form = CustomUserCreationForm(
            data={
                "username":"testuser",
                "email":"testuser@email.com",
                "first_name":"Test",
                "last_name":"User",
                "password1":"testpass123",
                "password2":"testpass123"
            }
        )

        self.assertTrue(
            form.is_valid()
        )

        user = form.save()

        self.assertEqual(
            user.username,
            "testuser"
        )

        self.assertEqual(
            user.email,
            "testuser@email.com"
        )

        self.assertEqual(
            user.first_name,
            "Test"
        )

        self.assertEqual(
            user.last_name,
            "User"
        )
        self.assertTrue(
            user.check_password("testpass123")
        )
        self.assertIsInstance(
            user,
            get_user_model()
        )

    def test_custom_user_creation_form_password_mismatch(self):
        form = CustomUserCreationForm(
            data={
                "username":"testuser",
                "email":"testuser@email.com",
                "first_name":"Test",
                "last_name":"User",
                "password1":"testpass123",
                "password2":"differentpass123"
            }
        )

        self.assertFalse(
            form.is_valid()
        )

        self.assertIn(
            "password2",
            form.errors
        )

    def test_custom_user_creation_form_missing_username(self):
        form = CustomUserCreationForm(
            data={
                "username":"",
                "email":"testuser@email.com",
                "first_name":"Test",
                "last_name":"User",
                "password1":"testpass123",
                "password2":"testpass123"
            }
        )

        self.assertFalse(
            form.is_valid()
        )

        self.assertIn(
            "username",
            form.errors
        )

    def test_custom_user_creation_form_without_email(self):
        form = CustomUserCreationForm(
            data={
                "username":"testuser",
                "email":"",
                "first_name":"Test",
                "last_name":"User",
                "password1":"testpass123",
                "password2":"testpass123"
            }
        )

        self.assertTrue(
            form.is_valid()
        )

        self.assertNotIn(
            "email",
            form.errors
        )

        user = form.save()

        self.assertEqual(
            user.email,
            ""
        )

    def test_custom_user_creation_form_password_too_short(self):
        form = CustomUserCreationForm(
            data={
                "username":"testuser",
                "email":"testuser@email.com",
                "first_name":"Test",
                "last_name":"User",
                "password1":"1234567",
                "password2":"1234567"
            }
        )

        self.assertFalse(
            form.is_valid()
        )

        self.assertIn(
            "password2",
            form.errors
        )

    def test_custom_user_creation_form_password_entirely_numeric(self):
        form = CustomUserCreationForm(
            data={
                "username":"testuser",
                "email":"testuser@email.com",
                "first_name":"Test",
                "last_name":"User",
                "password1":"12345678",
                "password2":"12345678"
            }
        )

        self.assertFalse(
            form.is_valid()
        )

        self.assertIn(
            "password2",
            form.errors
        )
        

