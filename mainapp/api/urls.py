from django.urls import path

from .api_views import (
    CategoryApiView,
    CustomersListApiView,
)

urlpatterns = [
    path('categories/<int:id>/', CategoryApiView.as_view(), name='categories'),
    path('customers/', CustomersListApiView.as_view(), name='customers_list'),
]
