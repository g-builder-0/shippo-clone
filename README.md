# ShippoClone - Multi-Carrier Shipping API

A Django REST Framework implementation investigating multi-carrier shipping rate APIs, inspired by Shippo's architecture.

## Project Purpose

This project follows an investigation-driven learning approach to understanding API product engineering in the logistics domain. I'm building a working system to understand the business constraints and technical decisions behind shipping APIs.

## Current Implementation

### Phase 1: Basic DRF Architecture ✅ Complete
- RateRequest model with carrier, service level, and pricing
- RESTful API endpoints for rate management
- DRF ViewSets with automatic CRUD operations
- Request flow tracing and validation

### Phase 2: Address & Parcel Models ✅ Complete
- Address model with complete shipping address fields
- Parcel model with dimensions and weight
- Shipment model with ForeignKey relationships
- Nested serializers for read/write operations
- API endpoints for addresses, parcels, and shipments

### Phase 3: Multi-Carrier Rate Shopping ✅ Complete
- Rate model with carrier and service level fields
- Mock carrier classes (FedEx, UPS, USPS) with pricing logic
- Distance and weight-based rate calculation
- Rate shopping endpoint returning sorted options from all carriers
- Comparison of 9 different shipping options per shipment

**Current Endpoints:**
- `POST /api/rates/` - Rate management
- `POST /api/addresses/` - Address CRUD
- `POST /api/parcels/` - Parcel CRUD
- `POST /api/shipments/` - Create shipments linking addresses and parcels
- `POST /api/shipments/{id}/get_rates/` - Get rates from all carriers

**Example: Create a Shipment**

Request:
```json
POST /api/shipments/
{
    "address_from_id": 1,
    "address_to_id": 2,
    "parcel_id": 1
}
```

Response (with nested data):
```json
{
    "id": 1,
    "address_from": {
        "id": 1,
        "name": "Harry",
        "street1": "122 Lumpy Lane",
        "city": "Chicago",
        "state": "IL",
        "zip_code": "87654",
        "country": "US"
    },
    "address_to": {
        "id": 2,
        "name": "Doug",
        "street1": "505 Confused Circle",
        "city": "Miami",
        "state": "FL",
        "zip_code": "12909",
        "country": "US"
    },
    "parcel": {
        "id": 1,
        "length": "10.00",
        "width": "8.00",
        "height": "6.00",
        "weight": "5.00"
    },
    "created_at": "2026-03-03T19:24:32Z"
}
```

**Example: Get Rates for a Shipment**

Request:
```json
POST /api/shipments/2/get_rates/
```

Response (9 rates sorted by price):
```json
[
    {
        "id": 7,
        "carrier": "usps",
        "service_level": "ground",
        "amount": "7.69",
        "currency": "USD",
        "estimated_days": 7
    },
    {
        "id": 4,
        "carrier": "ups",
        "service_level": "ground",
        "amount": "9.42",
        "currency": "USD",
        "estimated_days": 5
    },
    {
        "id": 1,
        "carrier": "fedex",
        "service_level": "ground",
        "amount": "10.11",
        "currency": "USD",
        "estimated_days": 4
    },
    ...
]
```

## Tech Stack

- **Django 6.0** - Web framework
- **Django REST Framework** - API toolkit
- **SQLite** - Database (development)
- **Python 3.13** - Programming language

## Setup

1. Clone the repository
```bash
git clone https://github.com/g-builder-0/shippo-clone.git
cd shippo-clone
```

2. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies
```bash
pip install django djangorestframework
```

4. Run migrations
```bash
python manage.py migrate
```

5. Start development server
```bash
python manage.py runserver
```

6. Access the API
- Browsable API: http://localhost:8000/api/shipments/
- Create addresses, parcels, and shipments through the interface
- Test rate shopping: http://localhost:8000/api/shipments/{id}/get_rates/

## Key Features

### Nested Serializers
The API uses DRF's nested serializer pattern:
- **Write operations:** Accept simple IDs (`address_from_id: 1`)
- **Read operations:** Return full nested objects with complete details

This mirrors how production APIs like Shippo work - simple input, detailed output.

### Multi-Carrier Rate Shopping
The rate shopping engine simulates how aggregators like Shippo work:
- Single API call returns rates from multiple carriers
- Pricing based on distance, weight, and service level
- Automatic sorting by price (cheapest first)
- Enables customers to compare options and choose best fit

### Model Relationships
Uses Django ForeignKey relationships to link shipments to addresses and parcels, enabling efficient queries and data integrity.

## Contributing

This is a personal learning project, but feedback on architecture decisions is welcome via issues.

## License

MIT

---

**Note:** This is a learning project demonstrating Django REST Framework skills for logistics API engineering roles. Not intended for production use.
