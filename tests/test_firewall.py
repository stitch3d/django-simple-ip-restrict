from django.test import TestCase


class TestFirewall(TestCase):
    def test_firewall(self):
        response = self.client.get("/admin/", HTTP_X_FORWARDED_FOR="83.4.12.1")
        self.assertEqual(response.status_code, 403)

    def test_firewall(self):
        response = self.client.get("/admin/", HTTP_X_FORWARDED_FOR="83.4.12.1, 10.2.1.1")
        self.assertEqual(response.status_code, 403)
