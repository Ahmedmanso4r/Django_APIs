"""
URL configuration for APIs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from books.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', list_books),
    path('books/create/', create_book, name='create_book'),
    path('books/show/<int:id>/', show_book, name='show_book'),
    path('books/update/put/<int:id>/', update_book_put, name='update_book_put'), 
    path('books/update/patch/<int:id>/', update_book_patch, name='update_book_patch'),
    path('books/delete/<int:id>/', delete_book, name='delete_book'),
]
