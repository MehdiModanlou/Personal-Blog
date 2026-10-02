from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserModelTests(TestCase):
    def test_custom_user_creation(self):
        user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@email.com",
            password="testpass123"
        )

        self.assertIsInstance(
                    user,
                    get_user_model()
                )

        self.assertEqual(
            user.username,
            "testuser"
        )

        self.assertEqual(
            user.email,
            "testuser@email.com"
        )

        self.assertTrue(
            user.check_password("testpass123")
        )

    def test_custom_user_is_active_by_default(self):
        user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@email.com",
            password="testpass123",
        )

        self.assertTrue(
            user.is_active
        )

    def test_custom_user_is_not_staff_default(self):
        user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@email.com",
            password="testpass123",
        )

        self.assertFalse(
            user.is_staff
        )

    def test_custom_user_is_not_superuser_by_default(self):
        user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@email.com",
            password="testpass123",
        )

        self.assertFalse(
            user.is_superuser
        )

    def test_custom_user_string_representation(self):
        user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@email.com",
            password="testpass123",
        )

        self.assertEqual(
            str(user),
            "testuser"
        )