from django.shortcuts import render
from django.views import View


class BaseSpecView(View):
    """Базовое отображение спецификаций"""
    def get(self, request, *args, **kwargs):
        return render(request, 'specs/product_features.html', {})