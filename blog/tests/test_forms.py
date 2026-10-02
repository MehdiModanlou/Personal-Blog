from datetime import datetime  # noqa: F401

from django.test import TestCase
from django.utils import timezone  # noqa: F401

from blog.forms import CommentForm, PostForm


class PostFormTests(TestCase):

    def test_post_form_valid(self):
        form_data = {
            "title": "title",
            "slug": "slug",
            "body": "body",
            "published": "2026-9-28 19:14:25",
        }
        form = PostForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_post_form_invalid_title(self):
        form_data = {
            "slug": "slug",
            "body": "body",
            "published": "2026-9-28 19:14:25",
        }
        form = PostForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_post_form_invalid_slug(self):
        form_data = {
            "title": "title",
            "slug": "slug slug",
            "body": "body",
            "published": "2026-9-28 19:14:25",
        }
        form = PostForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_post_form_fields(self):
        form = PostForm()

        self.assertIn("title", form.fields)
        self.assertIn("slug", form.fields)
        self.assertIn("published", form.fields)
        self.assertIn("categories", form.fields)
        self.assertIn("body", form.fields)


class CommentFormTests(TestCase):

    def test_comment_form_valid(self):
        form_data = {
            "body": "body"
        }
        form = CommentForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_comment_form_invalid(self):
        form_data = {}
        form = CommentForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_comment_form_field(self):
        form = CommentForm()

        self.assertIn("body", form.fields)
        self.assertNotIn("title", form.fields)

