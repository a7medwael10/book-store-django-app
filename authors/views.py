from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from authors.forms import AuthorForm
from authors.models import Author


class AuthorListView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'authors/index.html', context={'authors': authors})


class AuthorDetailView(View):
    def get(self, request, id):
        author = get_object_or_404(Author.objects.prefetch_related('books'), pk=id)
        return render(request, 'authors/show.html', context={'author': author})


class AuthorCreateView(View):
    def get(self, request):
        form = AuthorForm()
        return render(request, 'authors/create.html', context={'form': form})

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            messages.success(request, 'Author created successfully.')
            return redirect('authors.show', id=author.id)

        return render(request, 'authors/create.html', context={'form': form})


class AuthorUpdateView(View):
    def get(self, request, id):
        author = get_object_or_404(Author, pk=id)
        form = AuthorForm(instance=author)
        return render(request, 'authors/edit.html', context={'form': form, 'author': author})

    def post(self, request, id):
        author = get_object_or_404(Author, pk=id)
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save()
            messages.success(request, 'Author updated successfully.')
            return redirect('authors.show', id=author.id)

        return render(request, 'authors/edit.html', context={'form': form, 'author': author})


class AuthorDeleteView(View):
    def get(self, request, id):
        author = get_object_or_404(Author, pk=id)
        return render(request, 'authors/confirm_delete.html', context={'author': author})

    def post(self, request, id):
        author = get_object_or_404(Author, pk=id)
        author.delete()
        messages.success(request, 'Author deleted successfully.')
        return redirect('authors.index')
