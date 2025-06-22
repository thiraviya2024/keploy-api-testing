import unittest
import json
from app import app

class IntegrationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_item(self):
        response = self.app.post('/menu', json={
            "name": "Test Biryani",
            "category": "Main",
            "price": 150,
            "availability": "Yes"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Test Biryani', response.data)

    def test_get_menu(self):
        response = self.app.get('/menu')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_update_item(self):
        self.app.post('/menu', json={
            "name": "UpdateMe",
            "category": "Main",
            "price": 120,
            "availability": "Yes"
        })
        response = self.app.put('/menu/UpdateMe', json={
            "price": 130,
            "availability": "No"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Item updated', response.data)

    def test_delete_item(self):
        self.app.post('/menu', json={
            "name": "DeleteMe",
            "category": "Main",
            "price": 100,
            "availability": "Yes"
        })
        response = self.app.delete('/menu/DeleteMe')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Item deleted', response.data)

if __name__ == '__main__':
    unittest.main()
