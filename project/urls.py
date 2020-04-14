
from django.contrib import admin
from django.urls import path
from petra import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.ProductList.as_view(), name="product-list"),
    path('products/<int:product_id>',
         views.ProductDetail.as_view(), name="product-detail"),
    path('signup/', views.Register.as_view(), name="signup"),
    path('login/', TokenObtainPairView.as_view(), name="login"),
    path('create/<int:product_id>', views.Create.as_view(), name="create")
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)