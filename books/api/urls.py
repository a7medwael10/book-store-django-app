# from django.urls import path
# from .views import index, create, book_operations, books
from .routers import router

urlpatterns = [
    # path('', index),
    # path('create/', create),
    # path('<int:pk>/', book_operations),
    # path('model/', books),
] + router.urls