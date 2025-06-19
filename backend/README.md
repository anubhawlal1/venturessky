# Restaurant API Backend

This is the backend service for the restaurant management system, built with Django and Django REST Framework.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

## API Endpoints

- `GET /api/restaurants/` - List all restaurants
- `POST /api/restaurants/` - Create a new restaurant
- `GET /api/restaurants/{id}/` - Retrieve a specific restaurant
- `PUT /api/restaurants/{id}/` - Update a restaurant
- `DELETE /api/restaurants/{id}/` - Delete a restaurant

## Features

- RESTful API for restaurant management
- Data validation and serialization
- Order revenue calculation utility
- MQTT integration for real-time updates
- gRPC service for restaurant details
- Redis caching for improved performance 