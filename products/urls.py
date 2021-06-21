from django.urls import path
from .views import home_view, about_view, product_create_view, product_list_view, \
        product_detail_view,product_delete_view, product_update_view,ProductListView,ProductDetailView, \
        ProductCreateView, ProductDeleteView, ProductRawListView
app_name = "product"
urlpatterns = [
    path('' , ProductListView.as_view(), name='product_list'),
    path('type/' , ProductListView.as_view(template_name='product_list_view_type2.html'), name='product_list_type2'),
    path('<int:id>/detail/' , ProductRawListView.as_view(), name='product_detail'),
    # path('<int:id>/detail/' , product_list_view(), name='product_detail'),
    path('<int:id>/delete/' , ProductDeleteView.as_view(), name='product_delete'),
    path('<int:id>/update/' , product_update_view, name='product_update'),
    path('create/' , ProductCreateView.as_view(), name='product_create'),
]

