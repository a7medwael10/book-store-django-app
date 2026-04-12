from django.urls import path

from authors.views import (
    AuthorCreateView,
    AuthorDeleteView,
    AuthorDetailView,
    AuthorListView,
    AuthorUpdateView,
)

urlpatterns = [
    path('', AuthorListView.as_view(), name='authors.index'),
    path('create/', AuthorCreateView.as_view(), name='authors.create'),
    path('<int:id>/', AuthorDetailView.as_view(), name='authors.show'),
    path('<int:id>/edit/', AuthorUpdateView.as_view(), name='authors.edit'),
    path('<int:id>/delete/', AuthorDeleteView.as_view(), name='authors.delete'),
]
