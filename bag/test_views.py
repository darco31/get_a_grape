"""
Imports for the test on views app
"""
from django.test import TestCase
from products.models import Product


class TestViews(TestCase):
    """
    Tests for the bag app views
    """
    def test_bag_view(self):
        """
        Test for the bag view
        """
        response = self.client.get('/bag/')
        self.assertTemplateUsed(response, 'bag/bag.html')
        self.assertEqual(response.status_code, 200)

    def test_add_item_to_bag(self):
        """
        Test the add to bag
        """
        product = Product.objects.create(
            name='New Product',
            price='20.01',
            description='new product description',
            varietal='New type',
            image='new product test images',
            )

        response = self.client.post(f'/bag/add/{product.id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.id}/'})
        self.assertRedirects(response, f'/products/{product.id}/')

    def remove_item_from_bag(self):
        """
        Test the remove item from bag
        """
        product = Product.objects.create(
            name='New Product',
            price='20.01',
            description='new product description',
            varietal='New type',
            image='new product test images',
            )

        self.client.post(f'/bag/add/{product.id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.id}/'
        })

        response = self.client.get(f'/bag/remove/{product.id}/')
        bag = self.client.session['bag']

        self.assertEqual(bag, {})
        self.assertEqual(response.status_code, 200)
