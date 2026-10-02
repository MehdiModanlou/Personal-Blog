from django.test import SimpleTestCase
from django.urls import resolve

from blog.views import (
    CategorySlugView,
    CommentCreateView,
    CommentDeleteView,
    CommentUpdateView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostSearchView,
    PostUpdateView,
)


class PostUrlsTest(SimpleTestCase):
    def test_post_list_url(self):
        resolver = resolve("/")

        self.assertEqual(
            resolver.func.view_class,
            PostListView
        )

    def test_post_detail_url(self):
        resolver = resolve("/1/")

        self.assertEqual(
            resolver.func.view_class,
            PostDetailView
        )

    def test_post_create_url(self):
        resolver = resolve("/create/")

        self.assertEqual(
            resolver.func.view_class,
            PostCreateView
        )

    def test_post_update_url(self):
        resolver = resolve("/1/edit/")

        self.assertEqual(
            resolver.func.view_class,
            PostUpdateView
        )

    def test_post_delete_url(self):
        resolver = resolve("/1/delete/")

        self.assertEqual(
            resolver.func.view_class,
            PostDeleteView
        )

    def test_comment_create_url(self):
        resolver = resolve("/1/comment/create/")

        self.assertEqual(
            resolver.func.view_class,
            CommentCreateView
        )

    def test_comment_update_url(self):
        resolver = resolve("/1/comment/edit/")

        self.assertEqual(
            resolver.func.view_class,
            CommentUpdateView
        )

    def test_comment_delete_url(self):
        resolver = resolve("/1/comment/delete/")

        self.assertEqual(
            resolver.func.view_class,
            CommentDeleteView
        )

    def test_post_search_url(self):
        resolver = resolve("/search/")

        self.assertEqual(
            resolver.func.view_class,
            PostSearchView
        )

    def test_category_url(self):
        resolver = resolve("/category/test-1/")

        self.assertEqual(
            resolver.func.view_class,
            CategorySlugView
        )

