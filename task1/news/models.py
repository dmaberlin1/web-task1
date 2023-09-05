from django.db import models


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=40, blank=True)
    theme = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='created')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='updated')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    is_published = models.BooleanField(default=True,verbose_name='published')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'all news'
        ordering = ['-created_at', 'pk']
