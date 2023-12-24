from django.urls import path

from . import views

app_name = 'nau_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index_html, name='index_html'),
]


# app_name = 'myblog'
# urlpatterns = [
#     path('', views.index, name='index'),
# ]