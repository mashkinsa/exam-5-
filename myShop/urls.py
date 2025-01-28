from django.conf.urls.static import static
from django.urls import path

from .views import index, register, login_view, product_detail, product_list, profile, logout_view, edit_profile, create_product
from Shop import settings

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('create_product/', create_product, name='create_product'),
    path('logout/', logout_view, name='logout'),
    path('service/', product_list, name='product_list'),
    path('service/<int:product_id>/', product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)