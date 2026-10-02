from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", 
         views.PostListView.as_view(), 
         name="post_list"),
    path("<int:pk>/", 
         views.PostDetailView.as_view(), 
         name="post_detail"),
    path("create/", 
         views.PostCreateView.as_view(), 
         name="post_create"),
    path("<int:pk>/edit/", 
         views.PostUpdateView.as_view(),
         name="post_update"),
    path("<int:pk>/delete/",
         views.PostDeleteView.as_view(),
         name="post_delete"),
    path("category/<slug:slug>/",
         views.CategorySlugView.as_view(),
         name="category_slug"),
    path("<int:pk>/comment/create/",
         views.CommentCreateView.as_view(),
         name="comment_create"),
    path("<int:pk>/comment/delete/",
         views.CommentDeleteView.as_view(),
         name="comment_delete"),
    path("<int:pk>/comment/edit/",
         views.CommentUpdateView.as_view(),
         name="comment_update"),
     path("search/", 
          views.PostSearchView.as_view(),
          name="post_search"
          )
]