from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from collections import OrderedDict

from .serializers import CategorySerializers, CustomerSerializer

from ..models import Category, Customer


class CategoryPagination(PageNumberPagination):

    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('objects_count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('items', data)
        ]))


class CategoryApiView(ListCreateAPIView, RetrieveUpdateAPIView):

    serializer_class = CategorySerializers
    pagination_class = CategoryPagination
    queryset = Category.objects.all()
    lookup_field = 'id'


class CustomersListApiView(ListAPIView):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()