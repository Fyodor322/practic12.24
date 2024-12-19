from goods import views
from django.urls import path

app_name = 'goods'

urlpatterns = [
    path("", views.catalog, name='catalog'),
    path('product/', views.product, name='product'),
]
