from django.contrib import admin
from django.urls import path,include
from . import settings
from django.conf.urls.static import static
from azbankgateways.urls import az_bank_gateways_urls
from product.bank import go_to_gateway_view, callback_gateway_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('accounts.urls',namespace='accounts')),
    path('product/',include('product.urls',namespace='product')),
    path('',include('pages.urls',namespace='pages')),
    
    
    # bankgetways urls
    path('bankgateways/', az_bank_gateways_urls()),
    path('go-to-gateway/', go_to_gateway_view, name='go-to-gateway'),
    path('callback-gateway/', callback_gateway_view),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
