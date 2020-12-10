from decimal import Decimal
from unittest import mock

from django.test import TestCase, Client, RequestFactory
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Customer, Cart, CartProduct, Category, Notebook
from .views import recalc_cart, AddToCartView, BaseView


User = get_user_model()


class ShopTestCases(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.category = Category.objects.create(name='Ноутбуки', slug='notebooks')
        image = SimpleUploadedFile("notebook_image.jpg", content=b'', content_type="image/jpg")
        self.notebook = Notebook.objects.create(
            category=self.category,
            title="Test notebook",
            slug="test-notebook",
            image=image,
            price=Decimal("50000.00"),
            diagonal="17.3",
            display_type='IPS',
            processor_freq='3.4',
            ram='6 GB',
            video="Geforce GTX",
            time_without_charge="10 hour"
        )
        self.customer = Customer.objects.create(user=self.user, phone='1111111222', address='address')
        self.cart = Cart.objects.create(owner=self.customer)
        self.cart_product = CartProduct.objects.create(user=self.customer, cart=self.cart, content_object=self.notebook)


    #
    # def test_add_to_cart(self):
    #     self.cart.products.add(self.cart_product)
    #     recalc_cart(self.cart)
    #     self.assertIn(self.cart_product, self.cart.products.all())
    #     self.assertEqual(self.cart.products.count(), 1)
    #     self.assertEqual(self.final_price, '50000.00')

    # def test_response_from_add_to_cart_view(self):
    #     # client = Client()
    #     factory = RequestFactory()
    #     request = factory.get('')
    #     request.user = self.user
    #     response = AddToCartView.as_view()(request, ct_model="notebook", slug="test_slug")
    #
    #     # response = client.get('add-to-cart/notebook/test-slug/')
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/cart/')


    def test_mock_homepage(self):
        mock_data = mock.Mock(status_code=444)
        with mock.patch('mainapp.views.BaseView.get', return_value=mock_data) as mock_data_:
            factory = RequestFactory()
            request = factory.get('')
            request.user = self.user
            response = BaseView.as_view()(request)
            self.assertEqual(response.status_code, 444)
            print(mock_data_.called)
