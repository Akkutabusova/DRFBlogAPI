from django.conf.urls import url

from . import views
from .views import DeletePost, PostCategoriesList, PostListCategoryfilter, CategoryFavoritesfilter, Bookmarkfilter, \
    CreateBookmark, DeleteBookmark, CreateFavorite, DeleteFavorite, PostArrayDetail, CreatePostArray, EditPostArray, \
    DeletePostArray
from .views import PostList, PostDetail, PostListDetailfilter, CreatePost, AdminPostDetail, EditPost, CommentList, \
    CommentDetail, CreateComment, DeleteComment, PostCategoryDetail
# from rest_framework.routers import DefaultRouter
from django.urls import path, re_path

app_name = 'blog_api'

# router = DefaultRouter()
# router.register('', PostList, basename='post')
# urlpatterns = router.urls
# request http://127.0.0.1:8000/dept_emp/emp_list will invoke the emp_list function defined in views.py.

urlpatterns = [
    path('posts/<int:pk>', PostDetail.as_view(), name='detailcreate'),
    re_path('array/(?P<post>.+)/',  PostArrayDetail.as_view()),
    path('posts/', PostList.as_view(), name='listcreate'),
    path('search/', PostListDetailfilter.as_view(), name='postsearch'),
    # Bookmark
    path('bookmarks/', Bookmarkfilter.as_view(), name='listposts'),
    path('bookmarks/create', CreateBookmark.as_view(), name='createbookmark'),
    path('bookmarks/delete/<int:pk>', DeleteBookmark.as_view(), name='deletebookmark'),
    # Category
    re_path('category/(?P<category>.+)/$', PostListCategoryfilter.as_view()),  # posts by category
    path('categories/', PostCategoriesList.as_view(), name='listcategories'),#all categories
    path('categories/<int:pk>', PostCategoryDetail.as_view(), name='postsbycategory'),#category detail
    # Favorites
    path('favorites/', CategoryFavoritesfilter.as_view()),
    path('favorites/create', CreateFavorite.as_view()),
    path('favorites/delete/<int:pk>', DeleteFavorite.as_view()),
    # Comments
    # code omitted for brevity
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
    path('comments/create/', CreateComment.as_view()),
    path('comments/delete/<int:pk>/', DeleteComment.as_view()),
    # Post Admin Urls
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/array/create/', CreatePostArray.as_view(), name='createarray'),
    path('admin/edit/postdetail/<int:pk>', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/array/edit/<int:pk>/', EditPostArray.as_view(), name='editarray'),
    path('admin/delete/<int:pk>/', DeletePost().as_view(), name='deletepost'),
    path('admin/array/delete/<int:pk>/', DeletePostArray().as_view(), name='deletearray'),
]

