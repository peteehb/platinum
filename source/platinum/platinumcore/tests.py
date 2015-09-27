from django.test import TestCase

class ViewTests(TestCase):
    def test_index_page(self):
        response = self.client.get('/core/')
        self.assertEqual(response.status_code, 200)
