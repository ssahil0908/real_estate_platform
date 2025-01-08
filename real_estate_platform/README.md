

# Real Estate Property Listing API

## How to Start the Project

1. **Open the project in VSCode**.

2. **Install dependencies**:
```bash
   pip install -r requirements.txt
```

3. **Start the server**
```bash
   python -m uvicorn api:app --reload
```

# How to Use in Postman
1. **Create Property**

    --Description: This request creates a new property listing. The user_id is required as a query parameter.

    --Endpoint: POST /api/v1/properties

    --URL: 
```bash
      http://127.0.0.1:8000/api/v1/properties?user_id=user123
```
--Request Body (JSON):
```bash
       { "location": "New York",
          "price": 500000,
          "property_type": "Apartment",
          "description": "A beautiful apartment in the city center",
          "amenities": ["Pool", "Gym"]
       }        
```


2. **Search Properties**

    --Description: This will return properties that match the search criteria (price range and location).

    --Endpoint: GET /api/v1/properties/search

    --Query Parameters:

            1. min_price: Minimum price for filtering (optional).
            2.max_price: Maximum price for filtering (optional).
            3.location: Location for filtering (optional).

    --Example Request:

       http://127.0.0.1:8000/api/v1/properties/search?min_price=100000&max_price=600000&location=New York

3. **Get All Properties**

    --Description: This will return all properties in the system.

    --Endpoint: GET /api/v1/properties/search

    --URL:
```bash
     http://127.0.0.1:8000/api/v1/properties/search
```
