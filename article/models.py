# coding:utf-8
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)  # 文章题目
    category = models.CharField(max_length=50, blank=True)  # 文章标签
    date_time = models.DateTimeField(auto_now_add=True)  # 文章日期
    content = models.TextField(blank=True, null=True)  # 文章正文

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']