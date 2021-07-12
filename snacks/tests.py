from django.test import TestCase, SimpleTestCase
from django.urls import reverse

class test_Snack_page(TestCase):
    def test_status_code(self):
        self.assertEqual(self.client.get(reverse('index')).status_code, 200)

    def test_template_used(self):
        self.assertEqual(self.client.get(reverse('snacks_list')).templates[0].name ,'snacks_list.html')

        self.assertEqual(self.client.get(reverse('snacks_list')).templates[1].name ,'base.html')

