from datetime import datetime
import uuid

class Property:
    def __init__(self, property_id: str, user_id: str, details: dict):
        # Initialize property with basic details, status, and timestamp
        self.property_id = property_id
        self.user_id = user_id
        self.details = details
        self.status = "available"  # Default status
        self.timestamp = datetime.now()  # Time when the property was created

class PropertyManager:
    def __init__(self):
        # Initialize data structures
        self.properties = {}  # Store properties by ID
        self.user_portfolios = {}  # User's list of properties
        self.price_index = []  # List of price-indexed properties
        self.location_index = {}  # Properties indexed by location
        self.status_index = {"available": set(), "sold": set()}  # Set for status tracking

    def add_property(self, user_id: str, property_details: dict) -> str:
        # Create a new property, add to various indices, and return the property ID
        property_id = str(uuid.uuid4())
        property_obj = Property(property_id, user_id, property_details)
        self.properties[property_id] = property_obj

        # Add to user portfolio and update indices
        if user_id not in self.user_portfolios:
            self.user_portfolios[user_id] = []
        self.user_portfolios[user_id].append(property_id)
        self.price_index.append((property_details["price"], property_id))
        self.price_index.sort()  # Keep price index sorted
        if property_details["location"] not in self.location_index:
            self.location_index[property_details["location"]] = set()
        self.location_index[property_details["location"]].add(property_id)
        self.status_index["available"].add(property_id)

        return property_id

    def update_property_status(self, property_id: str, status: str, user_id: str) -> bool:
        # Update property status, ensure ownership and valid property ID
        if property_id not in self.properties:
            return False
        property_obj = self.properties[property_id]
        if property_obj.user_id != user_id:
            return False

        # Remove from old status and update to new status
        self.status_index[property_obj.status].remove(property_id)
        property_obj.status = status
        self.status_index[status].add(property_id)

        return True

    def get_user_properties(self, user_id: str) -> list:
        # Get all properties of a user, sorted by timestamp
        if user_id not in self.user_portfolios:
            return []
        user_property_ids = self.user_portfolios[user_id]
        return sorted(
            [self.properties[prop_id] for prop_id in user_property_ids],
            key=lambda x: x.timestamp,
            reverse=True
        )
