from django.core.validators import MinValueValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    breif = models.TextField()
    image = models.ImageField(upload_to='books/pictures/')
    author = models.ForeignKey('authors.Author', on_delete=models.SET_NULL, null=True, related_name='books')
    no_of_page = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title

