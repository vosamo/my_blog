# coding:utf-8
from django.db import models
from django.core.urlresolvers import reverse

class Article(models.Model):
    title = models.CharField(max_length=100)  # 文章题目
    category = models.CharField(max_length=50, blank=True)  # 文章标签
    date_time = models.DateTimeField(auto_now_add=True)  # 文章日期
    content = models.TextField(blank=True, null=True)  # 文章正文

    def get_absolute_url(self):
        path = reverse('detail', args=(1,))
        return "http://127.0.0.1:8000%s" % path

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']