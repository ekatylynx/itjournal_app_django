from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=170)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='media/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Category')

    def get_absolute_url(self):
        return reverse_lazy('view_news', kwargs={'news_id': self.pk})

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=170, db_index=True, verbose_name='Category title')

    # def get_absolute_url(self):
    #     return reverse_lazy('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']