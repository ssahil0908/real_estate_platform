from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import PropertyManager
from search import PropertySearch

app = FastAPI()  # Initialize FastAPI app
manager = PropertyManager()  # Initialize PropertyManager to handle properties
search = PropertySearch(manager)  # Initialize PropertySearch for searching/filtering properties


# Pydantic model to validate incoming property creation request data
class PropertyCreate(BaseModel):
    location: str  # Property location (required)
    price: float  # Property price (required)
    property_type: str  # Type of property (required)
    description: str  # Description of the property (required)


# API endpoint to create a new property listing
@app.post("/api/v1/properties")
async def create_property(property_data: PropertyCreate, user_id: str):
    try:
        # Add property using PropertyManager and return the generated property ID
        property_id = manager.add_property(user_id, property_data.dict())
        return {"property_id": property_id}
    except Exception as e:
        # Return an error response if property creation fails
        raise HTTPException(status_code=400, detail=str(e))


# API endpoint for searching properties with optional filters (price, location)
@app.get("/api/v1/properties/search")
async def search_properties(
    min_price: float = None,  # Minimum price filter
    max_price: float = None,  # Maximum price filter
    location: str = None,  # Location filter
    page: int = 1,  # Pagination page (defaults to 1)
    limit: int = 10  # Pagination limit (defaults to 10 results per page)
):
    # Create search criteria dictionary from query parameters
    criteria = {"price_min": min_price, "price_max": max_price, "location": location}
    
    # Use PropertySearch to get filtered properties
    properties = search.search_properties(criteria)
    
    # Pagination: slice the list based on the current page and limit
    start = (page - 1) * limit
    end = start + limit
    
    # Return the paginated results
    return properties[start:end]
