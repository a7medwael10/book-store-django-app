from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from books.forms import BookForm
from books.models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})


def show(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, 'books/show.html', {'book': book})


def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = Book.objects.create(
                title=form.cleaned_data['title'],
                breif=form.cleaned_data['breif'],
                image=form.cleaned_data['image'],
                no_of_page=form.cleaned_data['no_of_page'],
                price=form.cleaned_data['price'],
            )
            book.author = form.cleaned_data['author']
            messages.success(request, 'Book created successfully.')
            return redirect('books.index')
    else:
        form = BookForm()

    return render(request, 'books/create.html', {'form': form})


def edit(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        form.book_instance = book
        if form.is_valid():
            book.title = form.cleaned_data['title']
            book.breif = form.cleaned_data['breif']
            book.no_of_page = form.cleaned_data['no_of_page']
            book.price = form.cleaned_data['price']
            if form.cleaned_data.get('image'):
                book.image = form.cleaned_data['image']
            book.save()
            book.author = form.cleaned_data['author']
            messages.success(request, 'Book updated successfully.')
            return redirect('books.show', id=book.id)
    else:
        form = BookForm(
            initial={
                'title': book.title,
                'breif': book.breif,
                'no_of_page': book.no_of_page,
                'price': book.price,
                'author': book.author,
            },
        )
        form.book_instance = book

    return render(request, 'books/edit.html', {'book': book, 'form': form})

def delete(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully.')
    return redirect('books.index')
