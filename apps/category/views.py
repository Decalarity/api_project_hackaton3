from .models import Category
from .serializers import CategorySerializer
from rest_framework import generics
from django.contrib.auth import get_user_model

User = get_user_model()


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ['title']

    def get_serializer_context(self):
        return {'request': self.request}


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
