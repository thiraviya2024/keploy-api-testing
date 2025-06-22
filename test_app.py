import unittest
from app import create_item, menu

class TestMenuFunctions(unittest.TestCase):

    def setUp(self):
        # Clear the menu before each test
        menu.clear()

    def test_create_item(self):
        item = create_item("Paneer Butter Masala", "Main Course", 180, "Yes")
        self.assertEqual(item["name"], "Paneer Butter Masala")
        self.assertEqual(item["category"], "Main Course")
        self.assertEqual(item["price"], 180)
        self.assertEqual(item["availability"], "Yes")
        self.assertIn(item, menu)

    def test_multiple_items(self):
        item1 = create_item("Veg Biryani", "Main Course", 160, "Yes")
        item2 = create_item("Butter Naan", "Bread", 40, "Yes")
        self.assertEqual(len(menu), 2)
        self.assertIn(item1, menu)
        self.assertIn(item2, menu)

    def test_empty_menu(self):
        self.assertEqual(len(menu), 0)

if __name__ == '__main__':
    unittest.main()
