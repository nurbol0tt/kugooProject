from django.urls import path

from product.views import views_product

urlpatterns = [
    path('product/<int:pk>/detail/', views_product.ProductDetailView.as_view()),
    path('menu/', views_product.MenuListView.as_view()),
    path('home_banner/', views_product.BannerFilterHome.as_view()),
    path('techniques/', views_product.TechnicListView.as_view()),
    path('type_category/', views_product.TypeCategoryList.as_view()),
    path('cart_list/', views_product.CartProductList.as_view()),
]
