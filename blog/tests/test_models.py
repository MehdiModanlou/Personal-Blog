from django.contrib.auth import get_user_model
from django.test import TestCase

from blog.models import Category, Comment, Post


class PostModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='testpass123'
        )
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            body='This is a test post.',
            author=self.user,
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.slug, "test-post")
        self.assertEqual(self.post.body, "This is a test post.")
        self.assertEqual(self.post.author, self.user)

    def test_post_str(self):
        self.assertEqual(str(self.post), "Test Post")


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Django",
            slug='django'
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Django")
        self.assertEqual(self.category.slug, "django")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Django")


class CommentModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
                    username='testuser',
                    email='testuser@email.com',
                    password='testpass123'
                )
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            body='This is a test post.',
            author=self.user,
        )

        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body='This is a test comment'
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.author, self.user)
        self.assertEqual(self.comment.body, "This is a test comment")

    def test_comment_str(self):
        self.assertEqual(str(self.post.title), "Test Post")


