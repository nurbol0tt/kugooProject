from django.urls import path

from product.views import views_product

urlpatterns = [
    path('menu/', views_product.MenuListView.as_view()),
    path('home_banner/', views_product.BannerFilterHome.as_view()),
    path('popular_category/', views_product.TypeCategoryList.as_view()),
    path('catalog_list/', views_product.CatalogCategoryListView.as_view()),
    path('product_list/', views_product.ProductListView.as_view()),
    path('product/<int:pk>/like/', views_product.LikeView.as_view()),
]
