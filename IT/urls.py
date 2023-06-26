"""
URL configuration for SRKR project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from IT import views
from IT.views import Studentreg,Studentlist,Studentdetail,Studentupdate,Studentdelete
app_name='IT'
urlpatterns = [
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('product',views.product,name='product'),
    path('service',views.service,name='service'),
    #CBVpaths
    path('Studentreg',Studentreg.as_view(),name='Studentreg'),
    path('<pk>/Studentdetail',Studentdetail.as_view(),name='Studentdetail'),
    # path('',Studentlist.as_view(),name='Studentlist'),
    path('<pk>/Studentupdate',Studentupdate.as_view(),name='Studentupdate'),
    path('<pk>/Studentdelete',Studentdelete.as_view(),name='Studentdelete'),
    path('student',views.student, name = 'student'),
    path('form', views.form,name  = 'form'),
    path('detail/<int:id>', views.detail, name = 'detail'),
    path('update/<int:id>', views.update, name = 'update'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('',views.rit, name = ''),
    path('get1', views.get1, name = 'get1'),
    path('post1', views.post1, name = 'post1'),
    path('index', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('blog', views.blog, name = 'blog'),
    path('contact', views.contact, name = 'contact'),
    path('portfolio', views.portfolio, name = 'portfolio'),
    path('blog_single', views.blog_single, name = 'blog_single'),
    path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login'),
    path('logout', views.logoutuser, name = 'logout'),
]