class PropertySearch:
    def __init__(self, manager):
        self.manager = manager  # Store reference to PropertyManager

    def search_properties(self, criteria: dict) -> list:
        results = set(self.manager.status_index["available"])  # Start with available properties
        
        # Apply price range filter if both price_min and price_max are provided
        if "price_min" in criteria and criteria["price_min"] is not None and "price_max" in criteria and criteria["price_max"] is not None:
            results &= {prop_id for price, prop_id in self.manager.price_index
                        if criteria["price_min"] <= price <= criteria["price_max"]}
        
        # Apply location filter if provided
        if "location" in criteria:
            if criteria["location"] in self.manager.location_index:
                results &= self.manager.location_index[criteria["location"]]
        
        # Return properties matching the search criteria
        return [self.manager.properties[prop_id] for prop_id in results]

    def shortlist_property(self, user_id: str, property_id: str) -> bool:
        # Check if the property exists in the manager
        if property_id not in self.manager.properties:
            return False
        # Initialize user portfolio if not exists
        if user_id not in self.manager.user_portfolios:
            self.manager.user_portfolios[user_id] = set()
        # Add the property to the user's shortlist if not already added
        if property_id in self.manager.user_portfolios[user_id]:
            return False
        self.manager.user_portfolios[user_id].add(property_id)
        return True

    def get_shortlisted(self, user_id: str) -> list:
        # Return an empty list if the user has no shortlisted properties
        if user_id not in self.manager.user_portfolios:
            return []
        shortlisted = self.manager.user_portfolios[user_id]
        # Sort shortlisted properties by timestamp in descending order
        return sorted(
            [self.manager.properties[prop_id] for prop_id in shortlisted
             if self.manager.properties[prop_id].status == "available"],
            key=lambda x: x.timestamp,
            reverse=True
        )
