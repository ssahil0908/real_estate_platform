from models import PropertyManager
from search import PropertySearch

if __name__ == "__main__":
    # Initialize PropertyManager and PropertySearch
    manager = PropertyManager()
    search = PropertySearch(manager)

    # Example: Add a property
    user_id = "user1"  # User adding the property
    property_details = {"location": "NY", "price": 500000, "property_type": "Apartment"}  # Property details
    property_id = manager.add_property(user_id, property_details)  # Add property and get ID
    print(f"Property added with ID: {property_id}")

    # Example: Search properties based on criteria
    criteria = {"price_min": 300000, "price_max": 600000, "location": "NY"}  # Search criteria
    results = search.search_properties(criteria)  # Get search results
    print("Search results:", results)
