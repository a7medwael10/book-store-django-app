from decimal import Decimal

from django import forms

from authors.models import Author
from books.models import Book


class BookForm(forms.Form):
    title = forms.CharField(max_length=255)
    breif = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    image = forms.ImageField(required=False)
    no_of_page = forms.IntegerField(min_value=1)
    price = forms.DecimalField(max_digits=10, decimal_places=2, min_value=Decimal('0.01'))
    author = forms.ModelChoiceField(
        queryset=Author.objects.none(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.order_by('name')

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        query = Book.objects.filter(title=title)
        book_instance = getattr(self, 'book_instance', None)
        if book_instance:
            query = query.exclude(pk=book_instance.pk)
        if query.exists():
            raise forms.ValidationError('A book with this title already exists.')
        return title

    def clean_no_of_page(self):
        no_of_page = self.cleaned_data['no_of_page']
        if no_of_page <= 0:
            raise forms.ValidationError('Number of pages must be greater than 0.')
        return no_of_page

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError('Price must be greater than 0.')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        book_instance = getattr(self, 'book_instance', None)
        if not image and not (book_instance and book_instance.image):
            raise forms.ValidationError('Image is required.')
        return image
