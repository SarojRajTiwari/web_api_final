from django.db import models
from django.conf import settings


class News(models.Model):
    CATEGORY = (('0', 'Politics'),('1','Technologies'),('2','Sports'), ('3', 'Fashion'))
    title = models.CharField(max_length=255)
    article = models.TextField(verbose_name='Short and Sweet article!')
    slug = models.SlugField(max_length=255)
    category = models.CharField(choices=CATEGORY, max_length=2)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    cover_image = models.ImageField(upload_to='uploads')
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'newses'

    def __str__(self):
        return self.title
