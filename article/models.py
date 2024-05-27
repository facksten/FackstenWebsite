from django.db import models
from .choices import *
# Create your models here.

class ArticleCategory(models.Model):
    title = models.CharField(verbose_name="عنوان دسته بندی", max_length=100)
    description = models.TextField(verbose_name="توضیحات دسته بندی", null=True, blank=True)
    created_at = models.DateTimeField( verbose_name="تاریخ ساخت",auto_now_add=False)
    status = models.BooleanField(choices=ARTICLE_STATUS, default=True)


class Article(models.Model):
    title = models.CharField(verbose_name="عنوان مقاله", max_length=250)
    content = models.TextField(verbose_name="متن مقاله")
    status = models.BooleanField(verbose_name="وضعیت", choices=ARTICLE_STATUS, default=True)
    # author = models.ForeignKey(User, verbose_name=_(""), on_delete=models.CASCADE)
    category = models.ForeignKey(ArticleCategory, verbose_name="دسته بندی مقاله", on_delete=models.CASCADE)
    rate = models.IntegerField(verbose_name="امتیاز مقاله", default=0)
    slug = models.SlugField(verbose_name="اسلاگ مقاله", unique=True , max_length=100)
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False)
