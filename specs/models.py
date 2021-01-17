from django.db import models
from .utils import for_cyrillic_to_eng


class CategoryFeatures(models.Model):
    """Характеристика конкретной категории"""
    category = models.ForeignKey('mainapp.Category', verbose_name='Категория', on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=100, verbose_name='Имя характеристики')
    feature_filter_name = models.CharField(max_length=50, verbose_name='Имя для фильтра', blank=True)
    unit = models.CharField(max_length=50, verbose_name='Единица измерения', null=True, blank=True)
    
    class Meta:
        unique_together = ('category', 'feature_name', 'feature_filter_name')

    def __str__(self):
        return f'{self.category.name} | {self.feature_name}'

    def save(self, *args, **kwargs):
        if not self.feature_filter_name:
            self.feature_filter_name = for_cyrillic_to_eng(str(self.feature_name))
        super().save(*args, **kwargs)


class FeatureValidator(models.Model):
    """Валидатор значений для конкретной характеристики, принадлежащей конкретной категории"""
    category = models.ForeignKey('mainapp.Category', verbose_name='Категория', on_delete=models.CASCADE)
    feature_key = models.ForeignKey(
        CategoryFeatures, verbose_name='Ключ характеристика', on_delete=models.CASCADE)
    valid_feature_value = models.CharField(
        max_length=100, verbose_name='Валидное значение'
    )

    def __str__(self):
        # if not self.feature:
        #     return f'Валидатор категории "{self.category.name}" - характеристика не выбрана'
        return f'Категория "{self.category.name}" | ' \
               f'Характеристика - "{self.feature.feature_name}" | ' \
               f'Валидное значение - "{self.feature_value}"'


class ProductFeatures(models.Model):
    """Характеристкики продуктов"""
    product = models.ForeignKey('mainapp.Product', verbose_name='Товар', on_delete=models.CASCADE)
    feature = models.ForeignKey(CategoryFeatures, verbose_name='Характеристика', on_delete=models.CASCADE)
    value = models.CharField(max_length=255, verbose_name='Значение')

    def __str__(self):
        return f'Товар-"{self.product.title}" | ' \
               f'Характеристика - "{self.feature.feature_name}"' \
               f'Значение - {self.value}'
#
#
