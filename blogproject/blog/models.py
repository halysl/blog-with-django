# coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
	"""
    Django 要求模型必须继承 models.Model 类。
    Category 只需要一个简单的分类名 name 就可以了。
    CharField 指定了分类名 name 的数据类型，CharField 是字符型，
    CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
    Django 内置的全部类型可查看文档：
    https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
    """
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Tag(models.Model):
	'''
	Tag标签表，一个字段
	'''
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Post(models.Model):
	'''
	文章表，多个字段
	'''
	#标题
	title = models.CharField(max_length=100)

	#正文，使用TextField类型，大段文字
	body = models.TextField()

	#文章创建时间，最后一次修改时间，使用DateTimeField，一个时间
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()

	#文章摘要，可留空，字段属性blank == null
	excerpt = models.CharField(max_length=200,blank=True)

	#作者，User由django.contrib.auth.models导入
	#django.contrib.auth是django内置应用，处理网站部分流程
	#User 是 Django 为我们已经写好的用户模型
	author = models.ForeignKey(User)
	#根据分类及标签的属性，分配不同的数据类型
	#一篇文章对应一个分类，一个分类对应多个标签，一对多，所以用外键连category
	#一篇文章对应多个标签，一个标签对应多个文章，多对多，所以用ManyToManyField类型，可留空（blank=True）
	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag,blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'pk':self.pk})