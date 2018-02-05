from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm

def post_comment(request, post_pk):
	# 获取被评论的文章，以便在数据库中连接
	post = get_object_or_404(Post, pk=post_pk)

	# HTTP 请求有 get 和 post 两种，一般用户通过表单提交数据都是通过 post 请求
	if request.method == 'POST':
		form = CommentForm(request.POST)

		# is_valid()方法自动检测用户提交数据是否符合要求
		if form.is_valid():
			# save()方法先将用户的评论进行保存，commit=False 表明暂不保存到数据库
			comment = form.save(commit=False)

			# 将评论与文章关联
			comment.post = post

			# comments/models.py中的Comment类自带保存方法，存入数据库
			comment.save()

			# 重定向到 post 的详情页
			return redirect(post)

		else:
			comment_list = post.comment_set.all()
			context = {'post':post,
			           'form':form,
			           'comment_list':comment_list
			           }
			return render(request, 'blog/detail.html', context=context)

	# 若不是 post 请求，则说明用户没有提交数据，重定向到文章详情页
	return redirect(post)

