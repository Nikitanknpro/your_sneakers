from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('index', views.index, name='index_page'),
    path('login', views.login_view, name='login_page'),
    path('products', views.products_page, name='product_page'),
    path('products/create', views.product_create, name='product_create_page'),
    path('products/<int:id>', views.product_detail, name='product_detail_page'),
    path('products/brand/<int:id>', views.brand_products, name='brand_products'),
    path('brands', views.brand_view, name='brands_page'),
    path('cabinet', views.cabinet, name='cabinet'),
    path('logout', views.logout_view, name='logout_view'),
    path('reqister', views.reqister_view, name='reqister_view'),
]
