from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from blog.models import Category, Comment, Post


class PostListViewTest(TestCase):
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
            author=self.user,
            post=self.post,
            body="This is a test post."
        )

    def test_post_list_view(self):
        response = self.client.get(reverse("blog:post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_list.html")
        self.assertIn(self.post, response.context["posts"])
    
    def test_post_detail_view(self):
        response = self.client.get(reverse("blog:post_detail", args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_detail.html")
        self.assertEqual(response.context["post"], self.post)

    def test_post_create_view_authenticated(self):
        logged_in = self.client.login(
            username='testuser',
            password='testpass123'
        )
        self.assertTrue(logged_in)
        response = self.client.get(reverse("blog:post_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_create.html")

    def test_post_create_view_unauthenticated(self):
        response = self.client.get(reverse("blog:post_create"))
        self.assertRedirects(response, "/accounts/login/?next=/create/")

    def test_post_create_view_post(self):
        logged_in = self.client.login(
            username="testuser",
            password="testpass123"
        )
        self.assertTrue(logged_in)
        response = self.client.post(reverse("blog:post_create"),
                                    {
                                        "title": "title",
                                        "body": "body",
                                        "slug": "slug",
                                        "published": "2026-9-27 17:18:46"
                                    })
        self.assertRedirects(response, reverse("blog:post_list"))
        self.assertEqual(Post.objects.count(), 2)

        created_post = Post.objects.get(
            title="title",
            author=self.user
            )
        self.assertEqual(created_post.title, "title")
        self.assertEqual(created_post.author, self.user)

    def test_post_update_view_authenticated(self):
        logged_in = self.client.login(
            username="testuser",
            password="testpass123"
        )
        response = self.client.get(reverse("blog:post_update", args=[self.post.pk]))

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_update.html")
        self.assertEqual(response.context["form"]["title"].initial, self.post.title)
        self.assertEqual(response.context["form"]["body"].initial, self.post.body)
        self.assertEqual(response.context["form"]["slug"].initial, self.post.slug)

    def test_post_update_view_unauthenticated(self):
        response = self.client.get(
            reverse("blog:post_update", args=[self.post.pk])
        )

        self.assertRedirects(
            response,
            reverse("login") + "?next=" + reverse(
                "blog:post_update",
                args=[self.post.pk]
            )
        )

    def test_post_update_view_post(self):
        logged_in = self.client.login(
            username="testuser",
            password="testpass123",
        )
        response = self.client.post(
            reverse(
                "blog:post_update",
                args=[self.post.pk]
            ),
            {
                "title": "title",
                "body": "body",
                "slug": "slug",
                "published": "2026-9-27 17:18:46",
            }
        )

        self.assertTrue(logged_in)
        self.assertRedirects(
            response,
            reverse(
                "blog:post_list"
            )
        )

        self.assertEqual(
            Post.objects.count(),
            1
        )

        updated_post = Post.objects.get(pk=self.post.pk)
        self.assertEqual(
            updated_post.title,
            "title"

        )
        self.assertEqual(
            updated_post.slug,
            "slug"
        )
        self.assertEqual(
            updated_post.body,
            "body",
        )
        self.assertEqual(
            updated_post.author,
            self.user
        )

        expected_published = timezone.make_aware(
            datetime(2026, 9, 27, 17, 18, 46)  # noqa: DTZ001
        )
        self.assertEqual(
            updated_post.published,
            expected_published
        )

    def test_post_delete_view_authenticated(self):
        logged_in = self.client.login(
            username="testuser",
            password="testpass123"
        )
        response = self.client.get(
            reverse(
                "blog:post_delete",
                args=[self.post.pk]
            )
        )
        self.assertTrue(logged_in)
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertTemplateUsed(
            response,
            "blog/post_delete.html"
        )

    def test_post_delete_view_unauthenticated(self):
        response = self.client.get(
            reverse(
                "blog:post_delete",
                args=[self.post.pk]
            )
        )

        self.assertRedirects(
            response,
            reverse("login") + "?next=" + reverse(
                "blog:post_delete",
                args=[self.post.pk]
            )
        )

    def test_post_delete_view_post(self):
        logged_in = self.client.login(
            username="testuser",
            password="testpass123"
        )
        response = self.client.post(
            reverse(
                "blog:post_delete",
                args=[self.post.pk]
            )
        )
        self.assertTrue(logged_in)
        self.assertRedirects(
            response,
            reverse(
                "blog:post_list",
            )
        )
        self.assertEqual(
            Post.objects.count(),
            0
        )

    def test_post_update_view_other_user(self):
        user = get_user_model().objects.create_user(  # noqa: F841
            username="testuser1",
            password="testpass123"
        )
        logged_in = self.client.login(
            username="testuser1",
            password="testpass123"
        )
        response = self.client.get(
            reverse(
                "blog:post_update",
                args=[self.post.pk]
            )
        )

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 404)

    def test_post_delete_view_other_user(self):
        user = get_user_model().objects.create_user(  # noqa: F841
            username="testuser1",
            password="testpass123"
        )
        logged_in = self.client.login(
            username="testuser1",
            password="testpass123"
        )
        response = self.client.get(
            reverse(
                "blog:post_delete",
                args=[self.post.pk]
            )
        )
        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 404)

    def test_comment_create_view(self):
        logged_in = self.client.login(
            username="testuser",
            password="testpass123"
        )
        response = self.client.get(
            reverse(
                "blog:comment_create",
                args=[self.post.pk]
            )
        )

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/comment_form.html")

    def test_comment_create_view_post(self):
        logged_in = self.client.login(
            username="testuser",
            password="testpass123",
        )
        response = self.client.post(
            reverse(
                "blog:comment_create",
                args=[self.post.pk]
            ),
            {
                "body": "body"
            }
        )

        self.assertTrue(logged_in)
        self.assertRedirects(
            response,
            reverse(
                "blog:post_detail",
                args=[self.post.pk]
            )
        )
        self.assertEqual(
            Comment.objects.count(),
            2
        )

        create_comment = Comment.objects.get(body="body")

        self.assertEqual(
            create_comment.body,
            "body"
            
        )
        self.assertEqual(
            create_comment.author,
            self.user
        )
        self.assertEqual(
            create_comment.post,
            self.post
        )

    def test_comment_create_view_unauthenticated(self):
        response = self.client.get(
            reverse(
                "blog:comment_create",
                args=[self.post.pk]
            )
        )

        self.assertRedirects(
            response,
            reverse("login") + "?next=" + reverse(
                "blog:comment_create",
                args=[self.post.pk]
            )
        )

    def test_comment_update_view_authenticated(self):
        logged_in = self.client.login(
            username="testuser",
            password="testpass123",
        )
        response = self.client.get(
            reverse(
                "blog:comment_update",
                args=[self.comment.pk]
            )
        )

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "blog/comment_update.html"
        )

    def test_comment_update_view_other_user(self):
        logged_in = self.client.login(
            username="testuser",
            password="testpass123",
        )

        response = self.client.post(
            reverse(
                "blog:comment_update",
                args=[self.comment.pk],
            ),
            {
                "body": "Update comment body"
            }
        )

        self.assertTrue(logged_in)
        self.assertRedirects(
            response,
            reverse(
                "blog:post_detail",
                args=[self.post.pk]
            )
        )

        update_comment = Comment.objects.get(pk=self.comment.pk)

        self.assertEqual(
            update_comment.body,
            "Update comment body"
        )

    def test_comment_delete_view_authenticated(self):
        logged_id = self.client.login(
            username="testuser",
            password="testpass123",
        )

        response = self.client.get(
            reverse(
                "blog:comment_delete",
                args=[self.comment.pk]
            )
        )

        self.assertTrue(logged_id)
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertTemplateUsed(
            response,
            "blog/comment_delete.html"
        )

    def test_comment_delete_view_post(self):
        logged_in = self.client.login(
            username="testuser",
            password="testpass123",
        )

        response = self.client.post(
            reverse(
                "blog:comment_delete",
                args=[self.comment.pk]
            )
        )

        self.assertTrue(logged_in)

        self.assertRedirects(
            response,
            reverse(
                "blog:post_detail",
                args=[self.post.pk]
            )
        )

        self.assertEqual(
            Comment.objects.count(),
            0
        )

    def test_comment_delete_view_unathenticated(self):
        response = self.client.get(
            reverse(
                "blog:comment_delete",
                args=[self.comment.pk],
            ),
        )

        self.assertRedirects(
            response,
            reverse("login") + "?next=" + reverse(
                "blog:comment_delete",
                args=[self.comment.pk]
            )
        )

    def test_comment_delete_view_ownership(self):
        user = get_user_model().objects.create_user(  # noqa: F841
            username="testuser1",
            password="testpass123"
        )

        logged_in = self.client.login(
            username="testuser1",
            password="testpass123",
        )

        response = self.client.get(
            reverse(
                "blog:comment_delete",
                args=[self.comment.pk],
            ),
        )

        self.assertTrue(logged_in)

        self.assertEqual(
            response.status_code,
            404
        )

        self.assertEqual(
            Comment.objects.count(),
            1
        )

    def test_comment_update_view_unathenticated(self):
        response = self.client.get(
            reverse(
                "blog:comment_update",
                args=[self.comment.pk],
            ),
        )

        self.assertRedirects(
            response,
            reverse("login") + "?next=" + reverse(
                "blog:comment_update",
                args=[self.comment.pk]
            )
        )

    def test_comment_update_view_ownership(self):
        user = get_user_model().objects.create_user(  # noqa: F841
            username="testuser1",
            password="testpass123",
        )

        logged_in = self.client.login(
            username="testuser1",
            password="testpass123",
        )

        response = self.client.get(
            reverse(
                "blog:comment_update",
                args=[self.comment.pk],
            ),
        )

        self.assertTrue(logged_in)

        self.assertEqual(
            response.status_code,
            404
        )

        self.assertEqual(
            Comment.objects.count(),
            1
        )

    def test_post_detail_view_comments(self):
        response = self.client.get(
            reverse(
                "blog:post_detail",
                args=[self.post.pk],
            ),
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertIn(
            self.comment,
            response.context["comments"].object_list
        )

    def test_post_detail_view_comment_pagination(self):
        for i in range(5):
            Comment.objects.create(
                author=self.user,
                post=self.post,
                body=f"Comment {i}"
            )

        response = self.client.get(
            reverse(
                "blog:post_detail",
                args=[self.post.pk]
            )
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertEqual(
            Comment.objects.count(),
            6
        )

        self.assertEqual(
            len(response.context["comments"].object_list),
            5
        )

        self.assertTrue(
            response.context["comments"].has_next()
        )

    def test_post_detail_view_comment_pagination_second_page(self):
        for i in range(5):
            Comment.objects.create(
                author=self.user,
                post=self.post,
                body=f"Comment - {i}"
            )

        response = self.client.get(
            reverse(
                "blog:post_detail",
                args=[self.post.pk],
            ),
            {
                "page": 2
            }
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertEqual(
            response.context["comments"].number,
            2
        )

        self.assertEqual(
            len(response.context["comments"].object_list),
            1
        )

        self.assertTrue(
            response.context["comments"].has_previous()
        )

    def test_post_search_view(self):
        first_post = Post.objects.create(
            title="Django",
            slug="django",
            body="First post",
            author=self.user,
        )

        second_post = Post.objects.create(
            title="Python",
            slug="python",
            body="Django",
            author=self.user
        )

        third_post = Post.objects.create(
            title="Programming",
            slug="programming",
            body="Third post",
            author=self.user
        )

        response = self.client.get(
            reverse(
                "blog:post_search",
            ),
            {
                "q": "Django"
            }
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertIn(
            first_post,
            response.context["object_list"]
        )

        self.assertIn(
            second_post,
            response.context["object_list"]
        )

        self.assertNotIn(
            third_post,
            response.context["object_list"]
        )

    def test_post_search_view_no_query(self):
        response = self.client.get(
            reverse(
                "blog:post_search",
            )
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertEqual(
            len(response.context["object_list"]),
            0
        )

    def test_category_slug_view(self):
        category_1 = Category.objects.create(
            name="test 1",
            slug="test-1",
        )

        category_2 = Category.objects.create(
            name="test 2",
            slug="test-2",
        )

        post_1 = Post.objects.create(
            title="Django",
            slug="django",
            body="post 1",
            author=self.user,
        )

        post_2 = Post.objects.create(
            title="Python",
            slug="python",
            body="post 2",
            author=self.user,
        )

        post_1.categories.add(category_1)
        post_2.categories.add(category_2)

        response = self.client.get(
            reverse(
                "blog:category_slug",
                args=[category_1.slug],
            )
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertEqual(
            response.context["category"],
            category_1
        )

        self.assertIn(
            post_1,
            response.context["object_list"]
        )

        self.assertNotIn(
            post_2,
            response.context["object_list"]
        )

    def test_category_slug_view_invalid_slug(self):
        response = self.client.get(
            reverse(
                "blog:category_slug",
                args=["does-not-exist"],
            ),
        )

        self.assertEqual(
            response.status_code,
            404
        )


