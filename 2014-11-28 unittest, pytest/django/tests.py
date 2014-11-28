from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client

#run this test: python manage.py test twitter

class FirstTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login(self):
        self.assertEquals(reverse("sign_in"), '/signin/')
        response = self.client.get(reverse("sign_in"))
        self.assertEquals(response.status_code, 200)
        response = self.client.get(reverse("index"))
        self.assertEquals(response.status_code, 302)

        user = User.objects.create_user(
            username="user",
            password="user"
        )

        login_status = self.client.login(
            username='user',
            password='user'
        )

        self.assertTrue(login_status)

        response = self.client.get(reverse("sign_in"))
        self.assertEquals(response.status_code, 302)
        response = self.client.get(reverse("index"))
        self.assertEquals(response.status_code, 200)