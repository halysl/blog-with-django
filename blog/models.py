# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    name = models.CharField("分类名", max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name
    name = models.CharField("标签名", max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    title = models.CharField("标题", max_length=70)
    body = models.TextField("文章内容", )
    excerpt = models.CharField("文章摘要", max_length=200, blank=True)

    created_time = models.DateTimeField("创建时间", )
    modified_time = models.DateTimeField("修改时间", )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
