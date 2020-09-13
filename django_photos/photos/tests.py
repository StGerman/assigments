from django.test import TestCase, Client


class Registration(TestCase):

    client = Client()

    def test_my_view(self):
        data = {
            "username": "test",
            "email": "test@test.test",
            "password": "password",
            "password_confirmation": "password",
        }
        response = self.client.post("/register", data)
        print(response)
        assert response.status_code == 301
