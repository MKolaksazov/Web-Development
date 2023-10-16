from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, View
from .forms import EmailPostForm

#CLASS-based `views`

class PostListView(ListView): #analogous to the 'post_list' `view`
	queryset = Post.published.all()
	context_object_name = "posts"
	paginate_by = 3
	template_name = "blog/post/list.html"

#class PostShareView(View):

class PostDetailView(DetailView):
	queryset = Post.objects.all()
	context_object_name = "posts"
	template_name = "blog/post/detail.html"

#	model = Article

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		#return Post.published.filter(slug = self.request.slug)
		#context["now"] = timezone.now()
		return context
	def get_queryset(self):
		return self.queryset.filter(slug = self,
#status='published',
#publish__year=self.publish.year,
#publish__month=self.publish.month,
#publish__day=self.publish.day)
)
		#return context

#ORIGINAL (function-based) `views`

def post_share(request, post_id):
	post = get_object_or_404(Post, id=post_id, status='published')
	if request.method == 'POST':
		form = EmailPostForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
	else:
		form = EmailPostForm()
	return render(request, 'blog/post/share.html',
{'post': post, 'form': form})

def post_list(request): #RE-WRITTEN as `PostListView`
	object_list = Post.published.all()
	#posts = Post.published.all()
	paginator = Paginator(object_list, 3) #3 post on each page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger: #return first page if 'page' not integer
		posts = paginator.page(1)
	except EmptyPage: #return last page if page not here
		posts = paginator.page(paginator.num_pages)
	return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post, slug = post,
status='published',
publish__year=year,
publish__month=month,
publish__day=day)

	return render(request, 'blog/post/detail.html', {'post': post})




# Create your views here.
