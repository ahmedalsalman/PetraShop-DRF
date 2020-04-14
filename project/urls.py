
from django.contrib import admin
from django.urls import path
from petra import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('product-list/', views.ProductList.as_view(), name="product-list"),
    path('product-detail/<int:product_id>',
         views.ProductDetail.as_view(), name="product-detail"),
    path('signup/', views.Register.as_view(), name="signup"),
    path('login/', views.Login.as_view(), name="login"),
]