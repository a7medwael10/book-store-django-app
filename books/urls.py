from django.urls import path

from books.views import index, show, create, edit, delete

urlpatterns = [
    path('', index, name='books.index'),
    path('create/', create, name='books.create'),
    path('<int:id>/', show, name='books.show'),
    path('<int:id>/edit/', edit, name='books.edit'),
    path('<int:id>/delete/', delete, name='books.delete'),
]
