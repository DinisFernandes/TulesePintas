from django.urls import path, include
from .views import PostList, PostDetail, save_form, TodosList, PromoList, BestSalesList


urlpatterns = [
    path('', PostList.as_view(), name="post_list"),
    path('todos/', TodosList.as_view(), name="todos_list"),
    path('promocoes/', PromoList.as_view(), name="promo_list"),
    path('melhores-vendas/', BestSalesList.as_view(), name="bestsales_list"),
    path('post/<int:pk>/', PostDetail.as_view(), name="post_detail"),
    path('save-form/<int:id>/', save_form, name='save_form'),
    path('summernote/', include('django_summernote.urls')),
]