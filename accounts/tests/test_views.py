from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from accounts.forms import CustomUserCreationForm


class SignUpViewTests(TestCase):
    def test_signup_view_get(self):
        response = self.client.get(
            reverse(
                "accounts:signup"
            )
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertTemplateUsed(
            response,
            "accounts/signup.html"
        )

        self.assertIn(
            "form",
            response.context
        )

        self.assertIsInstance(
            response.context["form"],
            CustomUserCreationForm
        )

    def test_signup_view_post_valid(self):
        response = self.client.post(
            reverse(
                "accounts:signup"
            ),
            {
                "username": "testuser",
                "email": "testuser@email.com",
                "first_name": "Test",
                "last_name": "User",
                "password1": "testpass123",
                "password2": "testpass123"
            }
        )

        self.assertEqual(
            response.status_code,
            302
        )

        self.assertRedirects(
            response,
            reverse("login")
        )

        user = get_user_model().objects.get(
            username="testuser",
        )

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

    def test_signup_view_post_invalid(self):
        response = self.client.post(
            reverse(
                "accounts:signup"
            ),
            {
                "username": "testuser",
                "email": "testuser@email.com",
                "first_name": "Test",
                "last_name": "User",
                "password1": "testpass123",
                "password2": "differentpass123"
            }
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertTemplateUsed(
            response,
            "accounts/signup.html"
        )

        self.assertFalse(
            response.context["form"].is_valid()
        )

        self.assertIn(
            "password2",
            response.context["form"].errors
        )

        self.assertFalse(
            get_user_model().objects.filter(
                username="testuser"
            ).exists()
        )


class UserProfileViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@email.com",
            password="testpass123"
        )

    def test_user_profile_view_get(self):
        response = self.client.get(
            reverse(
                "accounts:userprofile",
                kwargs={"username": self.user.username}
            )
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertTemplateUsed(
            response,
            "accounts/profile_view.html"
        )

        self.assertEqual(
            response.context["object"],
            self.user
        )



