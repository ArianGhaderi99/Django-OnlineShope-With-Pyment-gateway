from django.urls import path
from product import views

app_name='product'

urlpatterns = [
    path('',views.product_view,name='product'),
    path('detail/<int:product_id>',views.product_detail,name='product_detail'),
    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('update-cart/',views.update_cart,name='update-cart'),
]