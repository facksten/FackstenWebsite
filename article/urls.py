from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dj_rest_auth.jwt_auth import get_refresh_view

router = DefaultRouter()
router.register('articlecategories', views.ArticleCategoryViewSet, basename="ArticleCategory")


urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)