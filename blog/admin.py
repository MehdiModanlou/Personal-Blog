from django.contrib import admin

from .models import Category, Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [  # noqa: RUF012
        "title",
        "slug",
        "author",
        "published",
    ]
    list_filter = [  # noqa: RUF012
        "author",
        "created",
        "published"
    ]
    search_fields = [  # noqa: RUF012
        "title",
        "author",
        "body",
    ]
    prepopulated_fields = {  # noqa: RUF012
        "slug": ("title",)
    }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [  # noqa: RUF012
        "name",
        "slug",
    ]
    search_fields = [  # noqa: RUF012
        "name",
    ]
    prepopulated_fields = {  # noqa: RUF012
        "slug": ("name",)
    }


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [  # noqa: RUF012
        "post",
        "author",
        "created",
    ]
    search_fields = [  # noqa: RUF012
        "post__title",
        "author__username",
        "body",
    ]
    list_filter = [  # noqa: RUF012
        "post",
        "created",
        "author"
    ]