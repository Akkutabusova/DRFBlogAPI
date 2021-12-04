from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return f'posts/{filename}'.format(filename=filename)


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(_("Image"), upload_to=upload_to, default='posts/default.jpg')
    objects = models.Manager()  # default manager

    def __str__(self):
        return self.name


class Favorites(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorite')
    category = models.ForeignKey('Category', related_name='favorite', on_delete=models.CASCADE)
    objects = models.Manager()  # default manager


class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    image = models.ImageField(_("Image"), upload_to=upload_to, default='posts/default.jpg')
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    date = models.CharField(max_length=250, default="12.12.12")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(
        max_length=10, choices=options, default='published')
    blog_views = models.IntegerField(default=0)
    week_views = models.IntegerField(default=0)
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title


class PostArray(models.Model):
    post = models.ForeignKey('Post', related_name='postarray', on_delete=models.CASCADE)
    index = models.IntegerField(default=0)
    image = models.ImageField(_("Image"), upload_to=upload_to, default='posts/default.jpg', null=True)
    text = models.TextField()
    objects = models.Manager()  # default manager


class Bookmark(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookmark')
    post = models.ForeignKey('Post', related_name='bookmark', on_delete=models.CASCADE)
    objects = models.Manager()  # default manager

    class Meta:
        ordering = ['created']


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    objects = models.Manager()  # default manager

    class Meta:
        ordering = ['created']
