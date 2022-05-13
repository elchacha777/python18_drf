"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from api.views import ProductViewSet, toggle_like, CommentViewSet

# Swagger
schema_view = get_schema_view(
    openapi.Info(
        title='Python18 API',
        default_version='v2',
        description='My API',
    ),
    public=True
)

# Распаковываем viewset
router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0)),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api/v2/', include(router.urls)),
    path('api/v2/products/<int:id>/toggle_like/', toggle_like)
]
