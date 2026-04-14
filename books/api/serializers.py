from rest_framework import serializers
from books.models import Book
from authors.models import Author
from authors.api.serializers import AuthorSerializer


# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=255)
#     breif = serializers.CharField()
#     image = serializers.ImageField()
#     no_of_page = serializers.IntegerField()
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     author_id = serializers.IntegerField(required=False, allow_null=True)

#     author = AuthorSerializer(read_only=True)

#     def validate_author_id(self, value):
#         if not Author.objects.filter(id=value).exists():
#             raise serializers.ValidationError("Author does not exist")
#         return value

#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.breif = validated_data.get('breif', instance.breif)
#         instance.image = validated_data.get('image', instance.image)
#         instance.no_of_page = validated_data.get('no_of_page', instance.no_of_page)
#         instance.price = validated_data.get('price', instance.price)
#         instance.author_id = validated_data.get('author_id', instance.author_id)
#         instance.save()
#         return instance
    
    
class BookModelSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        source='author',
        queryset=Author.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'breif',
            'image',
            'author',
            'author_id',
            'no_of_page',
            'price',
            'created_at',
            'updated_at',
        ]
