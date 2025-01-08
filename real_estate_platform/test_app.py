import unittest
from models import PropertyManager
from search import PropertySearch


class TestRealEstatePlatform(unittest.TestCase):
    def setUp(self):
        self.manager = PropertyManager()
        self.search = PropertySearch(self.manager)

    def test_add_property(self):
        property_details = {"location": "NY", "price": 500000, "property_type": "Apartment"}
        property_id = self.manager.add_property("user1", property_details)
        self.assertIn(property_id, self.manager.properties)

    def test_search_properties(self):
        property_details = {"location": "NY", "price": 500000, "property_type": "Apartment"}
        self.manager.add_property("user1", property_details)
        criteria = {"price_min": 400000, "price_max": 600000, "location": "NY"}
        results = self.search.search_properties(criteria)
        self.assertEqual(len(results), 1)


if __name__ == "__main__":
    unittest.main()
