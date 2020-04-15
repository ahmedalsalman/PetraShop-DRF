
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
    path('products/<int:product_id>/',views.ProductDetail.as_view(), name="product-detail"),
    path('signup/', views.Register.as_view(), name="signup"),
    path('login/', TokenObtainPairView.as_view(), name="login"),

    path('create/', views.Create.as_view(), name="create"),
    path('update/<int:product_id>/', views.Update.as_view(), name='update'),
    path('delete/<int:product_id>/', views.Delete.as_view(), name='delete'),
    path('cart/<int:cart_id>/', views.CartDetails.as_view(), name='cart-detail'),
    path('update/<int:cart_id>', views.CartUpdate.as_view(), name='cart-update')

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


