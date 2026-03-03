# ShippoClone - Multi-Carrier Shipping API

A Django REST Framework implementation investigating multi-carrier shipping rate APIs, inspired by Shippo's architecture.

## Project Purpose

This project follows an investigation-driven learning approach to understanding API product engineering in the logistics domain. Rather than following tutorials, I'm building a working system to understand the business constraints and technical decisions behind shipping APIs.

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

**Current Endpoints:**
- `POST /api/rates/` - Rate management
- `POST /api/addresses/` - Address CRUD
- `POST /api/parcels/` - Parcel CRUD
- `POST /api/shipments/` - Create shipments linking addresses and parcels

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
- Browsable API: http://localhost:8000/api/addresses/
- Create addresses, parcels, and shipments through the interface

## Key Features

### Nested Serializers
The API uses DRF's nested serializer pattern:
- **Write operations:** Accept simple IDs (`address_from_id: 1`)
- **Read operations:** Return full nested objects with complete details

This mirrors how production APIs like Shippo work - simple input, detailed output.

### Model Relationships
Uses Django ForeignKey relationships to link shipments to addresses and parcels, enabling efficient queries and data integrity.

## Contributing

This is a personal learning project, but feedback on architecture decisions is welcome via issues.

## License

MIT

---

**Note:** This is a learning project demonstrating Django REST Framework skills for logistics API engineering roles. Not intended for production use.
