from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.



# 接受用户的请求，采用标准的httpreponse返回数据
# def index(request):
#     # 这里处理模型
#     return HttpResponse("Hello World nau_dushaoxing!") # 模版

def index_html(request):
    # 这里处理模型
    return HttpResponse("Hello World in HTML!")  # 模版

# 参考 
# https://docs.djangoproject.com/zh-hans/4.1/intro/tutorial03/#a-shortcut-render
def index(request):
    blog_list = Article.objects.order_by('title')
    context = {'blog_list':blog_list}
    return render(request, 'blog2.html', context)

 