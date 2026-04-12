from rest_framework import serializers



class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    bio = serializers.CharField()
    gender = serializers.CharField(max_length=10)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)   