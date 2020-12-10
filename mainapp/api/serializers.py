from rest_framework import serializers

from ..models import Category, Customer, Order


class CategorySerializers(serializers.ModelSerializer):

    name = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = Category
        fields = [
            'id', 'name', 'slug'
        ]


class BaseProductSerializer:

    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects)
    title = serializers.CharField(required=True)
    slug = serializers.SlugField(required=True)
    image = serializers.ImageField(required=True)
    description = serializers.CharField(required=True)
    price = serializers.DecimalField(max_digits=9, decimal_places=2, required=True)


# class SmartphoneSerializer(BaseProductSerializer, serializers.ModelSerializer):
#
#     diagonal = serializers.CharField()  # required по умолчанию True, можно было не указывать
#     display_type = serializers.CharField()
#     resolution = serializers.CharField()
#     accum_value = serializers.CharField()
#     ram = serializers.CharField()
#     sd = serializers.BooleanField()
#     sd_volume_max = serializers.CharField()
#     store_max = serializers.CharField()
#     main_cam_mp = serializers.CharField()
#     frontal_cam_mp = serializers.CharField()
#
#     class Meta:
#         model = Smartphone
#         fields = '__all__'
#

# class NotebookSerializator(BaseProductSerializer, serializers.ModelSerializer):
#
#     diagonal = serializers.CharField()
#     display_type = serializers.CharField()
#     processor_freq = serializers.CharField()
#     ram = serializers.CharField()
#     video = serializers.CharField()
#     time_without_charge = serializers.CharField()
#
#     class Meta:
#         model = Notebook
#         fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):

    orders = OrderSerializer(many=True)

    class Meta:
        model = Customer
        fields = '__all__'


