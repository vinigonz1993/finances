from django.urls import path, include
from rest_framework_nested import routers
from categories.viewsets import (
    CategoriesViewSet
)


router = routers.DefaultRouter()
router.register(
    'categories',
    CategoriesViewSet,
    basename='list_categories'
)

urlpatterns = [
    path('backend/', include(router.urls)),
]
