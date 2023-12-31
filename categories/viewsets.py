from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin
)

from categories.models import Category
from categories.serializers import CategorySerializer


class CategoriesViewSet(
    GenericViewSet, ListModelMixin,
    CreateModelMixin
):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
