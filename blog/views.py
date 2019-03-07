from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost


def home(request):
    blogs = Blog.objects #쿼리 셋 #메소드
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list, 3) #블로그 객체 3개를 한 페이지로 구성
    page = request.GET.get('page') #request된 페이지를 알아냄
    posts = paginator.get_page(page) #request된 페이지를 얻어와 리턴(접근)
    return render(request, 'home.html', {'blogs' : blogs, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() #DB에 저장
    return redirect('/blog/'+str(blog.id)) #DB함수를 처리한다음 URL로 이동

def blogpost(request):
    #입력된 내용을 처리하는 기능
    #빈 페이지를 출력해주는 기능
    if request.method=='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})


# 쿼리셋과 메소드의 형식
# 모델.쿼리셋(objects).메소드
#.count() : 데이터갯수 반환
#.first() : 첫 번째 객체 반환
#.last() : 마지막 객체 반환


