from django.test import TestCase
from .models import Category, RegularPizza, SicilianPizza, Toppings, Sub, Pasta, Salad, DinnerPlatters, UserOrder, SavedCarts
from datetime import datetime, timedelta

class ModelTests(TestCase):
    def setUp(self):
        # Create test instances for models
        self.category = Category.objects.create(
            category_title='Test Category',
            category_gif='test.gif',
            category_description='Test category description'
        )

        self.regular_pizza = RegularPizza.objects.create(
            pizza_choice='Test Pizza',
            small_price=10.00,
            large_price=15.00,
            category_description='Test pizza description'
        )

        self.sicilian_pizza = SicilianPizza.objects.create(
            pizza_choice='Test Sicilian Pizza',
            small_price=12.00,
            large_price=18.00,
            category_description='Test Sicilian pizza description'
        )

        self.topping = Toppings.objects.create(
            topping_name='Test Topping'
        )

        self.sub = Sub.objects.create(
            sub_filling='Test Sub',
            small_price=8.00,
            large_price=12.00
        )

        self.pasta = Pasta.objects.create(
            dish_name='Test Pasta',
            price=7.00
        )

        self.salad = Salad.objects.create(
            dish_name='Test Salad',
            price=5.00
        )

        self.dinner_platter = DinnerPlatters.objects.create(
            dish_name='Test Platter',
            small_price=20.00,
            large_price=30.00
        )

        self.user_order = UserOrder.objects.create(
            username='test_user',
            order='Test order',
            price=25.00,
            time_of_order=datetime.now(),
            delivered=False
        )

        self.saved_cart = SavedCarts.objects.create(
            username='test_user',
            cart='Test saved cart'
        )

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Test Category')

    def test_regular_pizza_str(self):
        self.assertEqual(str(self.regular_pizza), 'Regular Pizza : Test Pizza')

    def test_sicilian_pizza_str(self):
        self.assertEqual(str(self.sicilian_pizza), 'Sicilian Pizza : Test Sicilian Pizza')

    def test_topping_str(self):
        self.assertEqual(str(self.topping), 'Test Topping')

    def test_sub_str(self):
        self.assertEqual(str(self.sub), 'Sub : Test Sub')

    def test_pasta_str(self):
        self.assertEqual(str(self.pasta), 'Test Pasta')

    def test_salad_str(self):
        self.assertEqual(str(self.salad), 'Salad : Test Salad')

    def test_dinner_platter_str(self):
        self.assertEqual(str(self.dinner_platter), 'Platter : Test Platter')

    def test_user_order_str(self):
        expected_str = f"Order placed by  : test_user on {datetime.now().date()} at {datetime.now().time().strftime('%H:%M:%S')}"
        self.assertEqual(str(self.user_order), expected_str)

    def test_saved_carts_str(self):
        self.assertEqual(str(self.saved_cart), 'Saved cart for test_user')






















































# Jesus I Trust in You
