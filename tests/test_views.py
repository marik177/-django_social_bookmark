from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.cache import cache
from django.urls import reverse


class AccountAuthTest(TestCase):
    def setUp(self):
        self.test_user = User.objects. \
            create_user(username='test_user',
                        password='test_password')
        self.non_auth_client = Client()
        self.auth_client = Client()
        self.auth_client.force_login(self.test_user)

    def tearDown(self):
        cache.clear()

    def test_unauthorized_user_cannot_access_dashboard_page(self):
        response = self.non_auth_client.get(reverse('dashboard'))
        self.assertNotEqual(response.status_code, 200)
        # and redirected to login page
        self.assertRedirects(response,
                             expected_url=
                             reverse('login')+'?next='+reverse('dashboard'))

    def test_authorized_user_can_access_dashboard_page(self):
        response = self.auth_client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_register_page_exists(self):
        response = self.non_auth_client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
