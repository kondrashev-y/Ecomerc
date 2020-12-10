from PIL import Image

from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.utils.safestring import mark_safe

from .models import *


class CleanImage():

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        # max_height, max_width = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Размер изображение не должен превышать 3MB!')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Разрешение изображения меньше минимального!')
        # if img.height > max_height or img.width > max_width:
        #     raise ValidationError('Разрешение изображения выше максимального!')
        return image


admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
