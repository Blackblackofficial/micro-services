from django.urls import path
from . import views

urlpatterns = [
    path('<str:orderItemUid>/warranty', views.warranty_solution),
    # path('<str:user_uid>/purchase', views.buy_order),
    # path('<str:user_uid>/<str:order_uid>', views.get_order),
    # path('<str:user_uid>/<str:order_uid>/warranty', views.get_order_warranty),
    # path('<str:user_uid>/<str:order_uid>/refund', views.get_order_refund)
]